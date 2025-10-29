# ANN – Aktivasiya Funksiyalarının Müqayisəsi (Sigmoid, ReLU, Tanh)

Bu repozitoriya **“Süni intellektin əsasları
”** fənni üzrə **sərbəst iş** kimi hazırlanmışdır.
Mövzu: **“Müxtəlif aktivləşmə funksiyalarının (Sigmoid, ReLU, Tanh) müqayisəli təhlili”**

Layihədə **sadə PyTorch modeli** vasitəsilə üç aktivasiya funksiyasının — **Sigmoid**, **Tanh** və **ReLU** — öyrənmə prosesinə təsiri **eyni şərtlərdə** müqayisə edilir.
Məsələ `scikit-learn` kitabxanasının `make_moons` dataseti üzərində **binary klassifikasiya** kimi qurulub.
Nəticələrdə **Loss** və **Accuracy** göstəricilərinin dövr üzrə dəyişməsi qrafiklərlə təqdim olunur.

Bu mövzu üzrə əlavə olaraq təqdimat (slayd) da hazırlanmışdır.

## Xüsusiyyətlər

- Eyni arxitektura: `2 → 10 → 1` (bir gizli qat)
- Fərqli aktivasiya funksiyaları: **Sigmoid**, **Tanh**, **ReLU**
- Eyni optimizer və hiperparametrlər: `Adam(lr=0.01)`, `epochs=200`
- İtki funksiyası: **MSELoss**
- Nəticələrdə **Loss** və **Accuracy** qrafikləri müqayisə edilir
- Reprodüsiya üçün **random seed** sabitlənir

## ⚙️ Tələblər

- **Uv**
- **Python 3.12**
- **PyTorch**
- **scikit-learn**
- **NumPy**
- **Matplotlib**

Qurulum (virtual mühit tövsiyə olunur):

```bash
uv sync
```

və ya:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

Bu layihə, neyron şəbəkələrdə aktivasiya funksiyalarının öyrənməyə və nəticə dəqiqliyinə təsirini praktiki şəkildə nümayiş etdirmək məqsədi daşıyır.
