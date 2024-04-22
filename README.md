![MasterHead](https://github.com/busecoban/IBM_CyberStart/assets/73944611/0f4de612-3ccc-4b13-b344-7dce9b455290)
<h1 align="center">IBM ile Kodluyoruz: CyberStart - 🐍 </h1>
<h3 align="center">“Yaratıcı bir fikrin iyi bir ağla buluşması, sıfırdan milyonlara gitmek için en iyi yoldur."</h3>


<h3 align="center">Jonah Peretti</h3>

# Hafta 1

### Genel Kültür
- El Harezmi , Algoritma , Cebir Kitabı
- Charles Babbage , Analitik Makine , girdileri ve çıktıları hesaplamak için bir dizi dişli, krank ve kıvılcım alıcısı
- Augusta Ada King , Charles Babbage'in Analitik Makine üzerindeki çalışmaları , bir bilgisayar tarafından işlenmek üzere yazılan ilk algoritma , ilk bilgisayar programcısı 
- 1950'lerde COBOL, FORTRAN ve BASIC  dilleri , bilgisayarların karmaşık işlemler yapması
- 1960'ların ve 1970'lerin ardından C ve Pascal dilleri , daha fazla kontrol ve esneklik  
- 1980'lerde, Apple ve Microsoft'un kişisel bilgisayarları , C++ ve Java
- 2000'lerde, web uygulamalarının yükselmesiyle JavaScript ve PHP , Python ve Ruby
  
### Python
#### Jupyter Notebook
##### The steps below shows how to install Jupyter on Mac : I use homebrew for quick and easy installation.
Step 1 — Install pyenv : Mac Os X come with Pythong 2.7 pre-installed but many Machine Learning packages are progressing to Python 3.x. Therefore, it’s recommended you start using Python 3 and the best way to do that is to first install pyenv version manager. This will allow you to install any version of Python you'd like.

First update Homebrew package manager.
```
brew update && brew doctor
```
Install pyenv version manager.
```
brew install pyenv
```
Step 2 — Install Python

Install Python 3.x using pyenv. You can see a list of version from Python Website.
```
pyenv install -l | grep -oE '[0-9]+\.[0-9]+\.[0-9]+'

pyenv install 3.10.4
```
Double check your work.
```
pyenv versions
```
You’ll also need to configure your ~/.bash_profile.
```
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```
Step 3 — Set Python to Local or Global
If you only want to use Python 3.x for a specific project, then cd to your specific directory and type:
```
pyenv local 3.x.x
```
If you’d prefer to just have Python 3.x installed globally throughout your operating system, then type:
```
pyenv global 3.x.x
```
Step 4 — Install Jupyter
Jupyter is an acronym for Julia, Python and R but these days, other languages are also included such as Ruby.
```
brew install jupyter
```
Step 5 — Start Jupyter
```
jupyter notebook
```

##### Jupyter Notebook shortcuts 
- dd delete 
- ctrl enter çalıştır
- shift enter çalıştır alta  geç
- a üste yeni cell 
- b üste yeni cell

#### Veri Tipleri

Veri objeleri ikiye ayrılır 
1)Scalar (Skaler): Tek bir değeri temsil eden veri tipleridir. Scalar veri tipleri şunlardır:
- int (Tam sayılar)
- float (Ondalık sayılar)
- complex (Karmaşık sayılar)
- bool (Boolean - Mantıksal değerler: True veya False)
- NoneType (None - boş değer)

2)Non-scalar (Skaler olmayan): Birden fazla değeri içeren ve birbiriyle ilişkili olan veri tipleridir. Non-scalar veri tipleri şunlardır:
- list (Listeler)
- tuple (Demetler)
- set (Kümeler)
- dict (Sözlükler)

#### Aritmetik Operatörler:
- +: Toplama
- -: Çıkarma
- *: Çarpma
- /: Bölme (gerçek sayı bölmesi)
- //: Bölme (tam sayı bölmesi)
- %: Mod (kalanı bulma)
- **: Üs alma

#### Karşılaştırma Operatörleri:
```

== Eşit mi?

!= Eşit değil mi?

<  Küçük mü?

>  Büyük mü?

<= Küçük veya eşit mi?

>= Büyük veya eşit mi?
```


#### Mantıksal Operatörler:
- and: VE
- or: VEYA
- not: DEĞİL

#### Atama Operatörleri:
- =: Değer atama
- +=: Toplama ve atama
- -=: Çıkarma ve atama
- *=: Çarpma ve atama
- /=: Bölme ve atama
- //=: Tam bölme ve atama
- %=: Mod ve atama
- **=: Üs alma ve atama

#### Üyelik Operatörleri:
- in: Bir öğe bir veri yapısında bulunuyor mu?
- not in: Bir öğe bir veri yapısında bulunmuyor mu?

#### Kimlik Operatörleri:
- is: İki nesnenin aynı nesne olup olmadığını kontrol eder.
- is not: İki nesnenin aynı nesne olmadığını kontrol eder.

#### print() Fonksiyonu:
```
x = 5
y = 10
print("x değeri:", x, "ve y değeri:", y)  # "x değeri: 5 ve y değeri: 10" çıktısını verir.
```
#### input() Fonksiyonu:
```
isim = input("Adınızı girin: ")
print("Merhaba,", isim)  # Kullanıcının girdiği ismi ekrana yazdırır.
```



### Clean Code

- Her dilin ve projenin kendi isimlendirme standartları vardır.Bunlara uymak, kodunuzun okunabilirliğini artırır.Python'da genellikle snake_case (örn. degisken_adi),Java'da ise camelCase (örn. degiskenAdi) kullanılır.
- Boolean değerleri temsil eden değişkenler genellikle bir durumu ifade eder. Bu tür değişkenler için is, has, can gibi ön ekler kullanmak kodun anlaşılırlığını artırır.
- Statik tipte, değişkenlerin türleri, değişkenler oluşturulurken belirlenir ve programın çalışma zamanı boyunca değiştirilemez. Bu, hataları daha erken yakalamamızı sağlar ve derleyici optimizasyonlarına olanak sağlar. Java, C, C++ ve Swift statik tipli dillere örnek olarak verilebilir.


Örneğin, Java'da bir değişken tanımlarken türünü belirtmemiz gerekmektedir:


```java


int sayi = 5;


```

- Dinamik tipte ise, değişkenlerin türü, programın çalışma zamanında belirlenir. Bu, daha az kod yazmamıza olanak sağlar ve daha esnek olmamızı sağlar. Ancak, bu esneklik tip hatalarını daha zor tespit edilebilir hale getirir. Python, Ruby, PHP ve JavaScript dinamik tipli dillere örnektir.


Python'da bir değişkeni tanımlarken, türünü belirtmemize gerek yoktur:


```python


sayi = 5


```

- Generic programlama, kodun belirli türlere bağımlı olmadan çalışabilmesini sağlar. Bu, kodun tekrar kullanılabilirliğini artırır ve tip güvenliğini sağlar. Generic'ler, statik tipli dillerin esneklik kazanmasına yardımcı olur. Java, C#, Swift gibi dillerde Generic programlama kullanılır.


Örneğin, Java'da bir liste oluştururken, listenin içinde ne tür bir veri tutacağını belirtmeliyiz:


```java


List<String> isimler = new ArrayList<String>();


```

- Ancak, bu liste sadece String türünde değerleri kabul eder. Eğer bizim bir liste oluşturmamız ve bu listenin farklı türleri kabul etmesi gerekiyorsa, generic'ler devreye girer:


```java


List<?> herTurluListe = new ArrayList<>();


```

### Tavsiyeler 

- Temiz kod hakkında daha fazla bilgi almak için Robert C. Martin'in "Clean Code" kitabını okumanızı öneririm. Ayrıca “teknik borç(technical debt)” ifadesini de araştırmanız güzel olabilir.

### Yazılım Alanlarını Tanıyalım





# Hafta 2

# Hafta 3

# Hafta 4

# Hafta 5

# Hafta 6


