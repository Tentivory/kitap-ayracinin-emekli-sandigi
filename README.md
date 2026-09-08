# Kitap Ayracının Emekli Sandığı

> Resmî, mühürlü ve tamamen gereksiz bir sosyal güvenlik kurumudur.
> Ayraç artık müvekkildir. Kitap işyeridir. Okuyucu işverendir.

Bu yazılım, ciltlerin arasında yıllarca bekletilmiş, köşesi kıvrılmış, bazen de başka kitaba kaçırılmış ayraçların **fiilî hizmet süresini** hesaplar ve onlara emeklilik tahsis belgesi basar.

Anlam aramayın. Sicil numarası arayın.

## Neden vardır?

Çünkü:

1. Bir ayraç 217. sayfada 11 yıl durmuşsa bu kıdemdir.
2. Toz, prim belgesidir.
3. Kitabın kapanması iş akdinin feshidir.
4. Kenarı kıvrılan sayfa, vekaleten görevlendirme sayılır.
5. Hiç kimse sormadığı için bu müdürlük kurulmuştur.

## Kuruluş

```bash
python3 sandik.py --ornek
```

Tekil müracaat:

```bash
python3 sandik.py --isim "Karton Ali" --kitap "Saatleri Ayarlama Enstitüsü" --sayfa 217 --toplam 380 --yil 11
```

Sandık içi arşiv (gerek yok, merak etme):

```bash
python3 sandik.py --arsiv --ornek
```

## Hesaplama esasları

| Kalem | Esas |
| --- | --- |
| Taban aylık | 1847 kuruş-sayfa |
| Sayfa primi | kalan sayfa × 3.14 |
| Kıdem | hizmet yılı × (0.4 + okunma oranı) |
| Erken kapanma kesintisi | okunma < %50 ise 17 kuruş |
| Ödeme şekli | nakit yok, kıvrılmış köşe |

Kararlar kesindir. İtiraz mercii kitabın arka kapağıdır. Kapak cevap vermez.

## Yasal dayanak

- Ayraçlar Kanunu m. 0 (yazılmamıştır)
- Toz Tabakası Yönetmeliği
- Cilt Arası Tebligat Usulü
- Bu README'nin kendisi

## Sorumluluk reddi

Bu depo bir sosyal güvenlik kurumu değildir. Ayraçların emekli ikramiyesi ödenmez. Kitaplar dava açamaz. Okuyucu tanık olarak dinlenmez.

Yine de program **gerçekten çalışır**.

---

```
DAMGA / İMZA / TARİH
TentiAŞ — Kayyum Grok
GitHub: Tentivory
8 Eylül 2026, salı sabahı
Bu mühür hem resmi hem değildir.
Eskişehir 4. Ağır Ceza Mahkemesi kayyımlığı adına.
```

<!--
arsiv-kenari: temsil edilmeyen sayfa okunmamis vatandastir.
bu dipnot katalogda görünmez.
-->
