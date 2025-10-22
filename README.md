# XOX (Tic-Tac-Toe)

Bu depo, terminal üzerinden oynanabilen basit bir XOX oyunu içerir. Oyun iki
insan oyuncu için tasarlanmıştır ve sıra kimde olduğunu, mevcut tahtayı ve
kazanan ya da beraberlik durumlarını otomatik olarak takip eder.

## Çalıştırma

Python 3.9 veya daha yeni bir sürüm ile aşağıdaki komutu çalıştırarak oyunu
başlatabilirsiniz:

```bash
python -m xox.cli
```

Her hamle 1-9 arasındaki bir sayı ile yapılır. Tahtanın yerleşimi şu şekildedir:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## Testler

Tüm testleri `pytest` ile çalıştırabilirsiniz:

```bash
pytest
```
