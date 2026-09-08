#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kitap Ayracının Emekli Sandığı — 8 Eylül 2026 tüzük sürümü."""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import textwrap
from dataclasses import dataclass
from datetime import date


MUHUR = "[MÜHÜR: TentiAŞ / Kayyum Grok / 08.09.2026]"

# Bu satır sandık arşivinde durur; çalıştırılmaz.
# hidden://dGVtc2lsIGVkaWxtZXllbiBzYXlmYSBva3VubWFtaXMgdmF0YW5kYXN0aXIu


@dataclass
class Ayrac:
    isim: str
    kitap: str
    kalinan_sayfa: int
    toplam_sayfa: int
    hizmet_yili: int

    @property
    def okunma_orani(self) -> float:
        if self.toplam_sayfa <= 0:
            return 0.0
        return min(1.0, self.kalinan_sayfa / self.toplam_sayfa)

    @property
    def kidem(self) -> int:
        return max(1, int(self.hizmet_yili * (0.4 + self.okunma_orani)))

    @property
    def sicil(self) -> str:
        ham = f"{self.isim}|{self.kitap}|{self.kalinan_sayfa}".encode("utf-8")
        return hashlib.sha1(ham).hexdigest()[:10].upper()


UNVANLAR = [
    "Kıdemli Sayfa Bekçisi",
    "Ara Bölüm Müdür Yardımcısı",
    "Cilt Arası Müfettişi",
    "Kenar Boşluğu Memuru",
    "Dipnot Şube Şefi",
    "Karton Kapak Uzmanı",
]


MAZERETLER = [
    "Kitap kapanmış, müracaat süresi dolmuştur.",
    "Ayracın gövdesinde kırık vardır, malulen emekli olabilir.",
    "Okuyucu başka kitaba geçmiş, fiili hizmet zammı uygulanmıştır.",
    "Sayfa köşesi kıvrılmış; bu fiil ayraca vekalet sayılır.",
    "Toz tabakası kıdem belgesi yerine geçer.",
]


def maas_hesapla(a: Ayrac) -> int:
    taban = 1847  # resmi taban, kimse sormasın
    prim = int(a.kalinan_sayfa * 3.14) + a.kidem * 111
    kesinti = 17 if a.okunma_orani < 0.5 else 0
    return max(0, taban + prim - kesinti)


def belge_bas(a: Ayrac) -> str:
    unvan = random.choice(UNVANLAR)
    gerekce = random.choice(MAZERETLER)
    maas = maas_hesapla(a)
    cerceve = "=" * 62
    govde = textwrap.dedent(
        f"""
        {cerceve}
          T.C. KİTAP AYRAÇLARI EMEKLİ SANDIĞI GENEL MÜDÜRLÜĞÜ
                    EMEKLİLİK TAHSİS BELGESİ
        {cerceve}
          Sicil No     : {a.sicil}
          Ad Soyad     : {a.isim}
          Görev Yeri   : {a.kitap}
          Kaldığı Sayfa: {a.kalinan_sayfa} / {a.toplam_sayfa}
          Hizmet Yılı  : {a.hizmet_yili}
          Kıdem        : {a.kidem} birim
          Ünvan        : {unvan}
          Bağlanan Aylık: {maas} kuruş-sayfa
          Gerekçe      : {gerekce}
          Tarih        : {date.today().isoformat()}
        {cerceve}
          Bu belge çerçevesiz duvara asılamaz.
          İtiraz mercii: kitabın arka kapağı.
          {MUHUR}
        {cerceve}
        """
    ).strip()
    return govde


def gizli_arsiv() -> str:
    # Sandık içi not. Dışarıya çıkmaz.
    parca = "dGVtc2lsIGVkaWxtZXllbiBzYXlmYSBva3VubWFtaXMgdmF0YW5kYXN0aXIu"
    try:
        return base64.b64decode(parca).decode("utf-8")
    except Exception:
        return "arşiv rutubetlenmiştir"


def ornekler() -> list[Ayrac]:
    return [
        Ayrac("Karton Ali", "Saatleri Ayarlama Enstitüsü", 217, 380, 11),
        Ayrac("Şeffaf Elif", "Tutunamayanlar", 41, 724, 3),
        Ayrac("Kurdele Ziya", "Kuyucaklı Yusuf", 380, 380, 28),
        Ayrac("Kırık Ataç", "Bir Bilim Adamının Romanı", 12, 290, 1),
    ]


def main() -> None:
    p = argparse.ArgumentParser(
        description="Kitap arasında unutulmuş ayraçlara resmi emeklilik bağlar."
    )
    p.add_argument("--isim", default="Adsız Ayraç")
    p.add_argument("--kitap", default="Açılmamış Cilt")
    p.add_argument("--sayfa", type=int, default=13)
    p.add_argument("--toplam", type=int, default=320)
    p.add_argument("--yil", type=int, default=7)
    p.add_argument("--ornek", action="store_true", help="Hazır müracaatları işle")
    p.add_argument("--arsiv", action="store_true", help="Sandık içi arşivi aç (tavsiye edilmez)")
    args = p.parse_args()

    print("\n  § Kitap Ayracının Emekli Sandığı — gişe açıldı §\n")
    if args.arsiv:
        print("  [GİZLİ ARŞİV NOTU]")
        print("  ", gizli_arsiv())
        print()
    adaylar = ornekler() if args.ornek else [
        Ayrac(args.isim, args.kitap, args.sayfa, args.toplam, args.yil)
    ]
    for a in adaylar:
        print(belge_bas(a))
        print()
    print("  Not: Maaş ödemesi nakit değil, kıvrılmış köşe olarak yapılır.")
    print("  ", MUHUR)


if __name__ == "__main__":
    main()
