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

#### print() Fonksiyonu:
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
#### Python String İfadeleri

Python'da string (dize) veri tipi metin verilerini temsil etmek için kullanılır. Bir string, karakterlerin birleşimidir ve tek tırnak (`'`) veya çift tırnak (`"`) içinde tanımlanır.

##### String Tanımlama

```python
s1 = 'Hello, world!'     # Tek tırnak içinde string
s2 = "Python Programming"   # Çift tırnak içinde string
s3 = """Bu çoklu
satırlı bir stringdir."""   # Üç çift tırnak içinde çok satırlı string
```

#### String Birleştirme (Concatenation)
```
s1 = "Hello"
s2 = "world"
s3 = s1 + " " + s2   # "Hello world" stringini oluşturur
```

#### String Dizinleme (Indexing) ve Dilimleme (Slicing)
```
s = "Python"
print(s[0])    # 'P' - İlk karakter
print(s[-1])   # 'n' - Son karakter
print(s[2:4])  # 'th' - 2. indeksten 4. indekse (dahil değil) kadar dilimleme
```

#### String Uzunluğu
```
s = "Python Programming"
print(len(s))  # 18 - stringin karakter sayısı
```

#### String Metodları
```
s = "hello, world!"
print(s.upper())   # Tüm karakterleri büyük harfe dönüştürür
print(s.lower())   # Tüm karakterleri küçük harfe dönüştürür
print(s.capitalize())  # Stringin ilk karakterini büyük harfe dönüştürür
print(s.split(","))   # Belirtilen bir ayraçla stringi böler
```

#### String Formatlama
```
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# "My name is Alice and I am 30 years old." çıktısını verir
```
veya 
```
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# "My name is Alice and I am 30 years old." çıktısını verir
```

#### comment
```
# Bu bir yorumdur
print("Hello, world!")  # Bu da bir yorumdur

# print("Bu kod çalışmayacak")
```

### short-circuit

Python'da kısa devre (short-circuit) değerlendirme, mantıksal operatörlerin (and, or) kullanımında gerçekleşen bir özelliktir. Kısa devre, bir ifadeyi değerlendirirken, sonucun zaten bilindiği durumlarda diğer ifadelerin değerlendirilmesini atlamaktır.

#### and Operatörü Kısa Devre
```
# Kısa devre olmayan durum
x = 5
y = 0
if x > 0 and x / y > 2:
    print("Bu satır çalışmayacak")
else:
    print("Kısa devre meydana geldi")

# Kısa devreli durum
x = 5
y = 0
if y != 0 and x / y > 2:
    print("Bu satır çalışmayacak")
else:
    print("Kısa devre meydana geldi")
```

#### or Operatörü Kısa Devre
```
# Kısa devre olmayan durum
x = 0
y = 5
if x == 0 or y / x > 2:
    print("Bu satır çalışmayacak")
else:
    print("Kısa devre meydana geldi")

# Kısa devreli durum
x = 0
y = 5
if x != 0 or y / x > 2:
    print("Kısa devre meydana geldi")
else:
    print("Bu satır çalışmayacak")
```

Yukarıdaki örneklerde, and operatöründe eğer ilk ifade False ise ikinci ifadeyi değerlendirmeye gerek kalmaz. Benzer şekilde, or operatöründe eğer ilk ifade True ise ikinci ifadeyi değerlendirmeye gerek kalmaz. Bu durum kısa devre (short-circuit) olarak adlandırılır. Bu özellik, kodun daha verimli ve hızlı çalışmasını sağlar.

#### if else elif
```
x = 10

if x > 0:
    print("x pozitif")
elif x == 0:
    print("x sıfır")
else:
    print("x negatif")
```

#### ternary conditions
```
# Ternary ifade kullanmadan
x = 5
if x > 0:
    result = "positive"
else:
    result = "non-positive"
print(result)  # "positive" çıktısını verecek

# Ternary ifade kullanarak
x = 5
result = "positive" if x > 0 else "non-positive"
print(result)  # "positive" çıktısını verecek
```

#### for Döngüsü:
```
# Liste üzerinde döngü
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Liste yerine bir string üzerinde döngü
for letter in "Python":
    print(letter)

# Belirli bir aralıkta döngü
for i in range(5):
    print(i)

# Belirli bir aralıkta belirli bir artış miktarı ile döngü
for i in range(0, 10, 2):
    print(i)
```

#### while Döngüsü:
```
# Belirli bir koşul sağlandığı sürece döngü
i = 0
while i < 5:
    print(i)
    i += 1

# Sonsuz döngü (Ctrl + C ile durdurulmalı)
# while True:
#     print("Sonsuz döngü")
```

#### break ifadesiyle döngüden çıkılır:
```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
```
#### continue ifadesiyle döngünün bir sonraki iterasyonuna geçilir:
```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
```

#### Liste Oluşturma:
```
# Boş liste oluşturma
my_list = []

# Stringlerden oluşan bir liste oluşturma
fruits = ["apple", "banana", "cherry"]

# Sayılardan oluşan bir liste oluşturma
numbers = [1, 2, 3, 4, 5]

# Farklı veri tiplerinden oluşan bir liste oluşturma
mixed_list = [1, "apple", True, 2.5]
```
#### Liste Elemanlarına Erişme:
```
fruits = ["apple", "banana", "cherry"]

# Belirli bir indeksteki elemana erişme
print(fruits[0])  # "apple"

# Negatif indekslerle son elemana erişme
print(fruits[-1])  # "cherry"

# Bir aralıktaki elemanlara erişme (dilimleme)
print(fruits[1:3])  # ["banana", "cherry"]

# Listeyi tersine çevirme
print(fruits[::-1])  # ["cherry", "banana", "apple"]
```
#### Liste Metodları:
```
fruits = ["apple", "banana", "cherry"]

# Liste uzunluğunu alma
print(len(fruits))  # 3

# Listenin sonuna eleman ekleme
fruits.append("orange")
print(fruits)  # ["apple", "banana", "cherry", "orange"]

# Belirli bir indekse eleman ekleme
fruits.insert(1, "grape")
print(fruits)  # ["apple", "grape", "banana", "cherry", "orange"]

# Belirli bir indeksteki elemanı silme
fruits.pop(1)
print(fruits)  # ["apple", "banana", "cherry", "orange"]

# Belirli bir değere sahip tüm elemanları silme
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "orange"]

# Liste elemanlarını sıralama
fruits.sort()
print(fruits)  # ["apple", "cherry", "orange"]

# Liste elemanlarını tersine sıralama
fruits.reverse()
print(fruits)  # ["orange", "cherry", "apple"]
```

#### tuple
Python'da tuple, değiştirilemez (immutable) bir veri yapısıdır. Tuple, virgülle ayrılmış öğelerden oluşur ve genellikle parantez içinde tanımlanır. İşte tuple oluşturma ve kullanma örnekleri:

#### Tuple Oluşturma:
```
# Boş tuple oluşturma
my_tuple = ()

# Tek bir eleman içeren tuple oluşturma
my_singleton_tuple = (1,)  # Tek elemanlı bir tuple tanımlarken virgül kullanılmalıdır.

# Stringlerden oluşan bir tuple oluşturma
fruits = ("apple", "banana", "cherry")

# Sayılardan oluşan bir tuple oluşturma
numbers = (1, 2, 3, 4, 5)

# Farklı veri tiplerinden oluşan bir tuple oluşturma
mixed_tuple = (1, "apple", True, 2.5)
```

#### Tuple Elemanlarına Erişme:
```
fruits = ("apple", "banana", "cherry")

# Belirli bir indeksteki elemana erişme
print(fruits[0])  # "apple"

# Negatif indekslerle son elemana erişme
print(fruits[-1])  # "cherry"

# Bir aralıktaki elemanlara erişme (dilimleme)
print(fruits[1:3])  # ("banana", "cherry")

# Tuple'ın uzunluğunu alma
print(len(fruits))  # 3
```

#### Tuple Metodları:
Tuple'lar değiştirilemez olduğundan, tuple veri yapısı üzerinde değişiklik yapmak mümkün değildir. Ancak, index() ve count() gibi bazı metodlar kullanılabilir:
```
fruits = ("apple", "banana", "cherry")

# Belirli bir değerin indeksini alma
print(fruits.index("banana"))  # 1

# Belirli bir değerin tuple içinde kaç defa geçtiğini alma
print(fruits.count("cherry"))  # 1
```

#### set
Python'da bir set, benzersiz ve değiştirilebilir (mutable) bir koleksiyon veri tipidir. Bir set, süslü parantezler {} içinde virgülle ayrılmış öğelerden oluşur. Set'ler, bir liste veya tuple gibi sıralı değildir ve öğeler arasında sıralama garantisi vermez. Ayrıca, bir set içinde aynı öğeden yalnızca bir tane bulunabilir. İşte set oluşturma ve kullanma örnekleri:

#### Set Oluşturma:
```
# Boş bir set oluşturma
my_set = set()

# Elemanlarıyla bir set oluşturma
my_set = {1, 2, 3, 4, 5}

# Bir liste veya tuple'dan bir set oluşturma
my_set = set([1, 2, 3, 4, 5])
```
#### Set Elemanlarına Erişme:
Set'lerde indeksleme veya dilimleme yapılamaz çünkü set'ler sıralı değildir. Ancak, bir elemanın bir set içinde bulunup bulunmadığını kontrol etmek için in operatörü kullanılabilir.

```
my_set = {1, 2, 3, 4, 5}

# Bir elemanın set içinde bulunup bulunmadığını kontrol etme
print(3 in my_set)  # True
print(6 in my_set)  # False

```

#### Set Metodları:
```
my_set = {1, 2, 3}

# Bir elemanı set'e ekleme
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# Bir elemanı set'ten silme
my_set.remove(2)
print(my_set)  # {1, 3, 4}

# Set'i temizleme
my_set.clear()
print(my_set)  # set()
```

#### dictionary 
Python'da bir sözlük (dictionary), anahtar-değer çiftlerini depolayan bir veri yapısıdır. Sözlükler, süslü parantezler {} içinde tanımlanır ve her bir öğe anahtar ve değer olarak adlandırılan bir çiftle temsil edilir. İşte sözlük oluşturma ve kullanma örnekleri:

#### Sözlük Oluşturma:
```
# Boş bir sözlük oluşturma
my_dict = {}

# Anahtarlar ve değerlerle bir sözlük oluşturma
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

# dict() fonksiyonu kullanarak bir sözlük oluşturma
my_dict = dict(apple=1, banana=2, cherry=3)

# Liste veya tuple kullanarak bir sözlük oluşturma
my_dict = dict([("apple", 1), ("banana", 2), ("cherry", 3)])
```

#### Sözlük Elemanlarına Erişme:
```
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

# Bir anahtara karşılık gelen değeri alma
print(my_dict["banana"])  # 2

# Bir anahtara karşılık gelen değeri get() metoduyla alma
print(my_dict.get("cherry"))  # 3

# Bir anahtara karşılık gelen değeri varsayılan bir değerle alma
print(my_dict.get("orange", "Varsayılan değer"))  # Varsayılan değer
```

#### Sözlük Metodları:
```
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

# Bir anahtarın varlığını kontrol etme
print("banana" in my_dict)  # True

# Bir anahtarın varlığını kontrol etme (get() metoduyla)
print(my_dict.get("orange") is not None)  # False

# Bir anahtara karşılık gelen değeri değiştirme
my_dict["banana"] = 5
print(my_dict)  # {'apple': 1, 'banana': 5, 'cherry': 3}

# Yeni bir anahtar-değer çifti ekleme
my_dict["orange"] = 4
print(my_dict)  # {'apple': 1, 'banana': 5, 'cherry': 3, 'orange': 4}

# Bir anahtarı ve karşılık gelen değeri silme
del my_dict["cherry"]
print(my_dict)  # {'apple': 1, 'banana': 5, 'orange': 4}

# Tüm anahtar-değer çiftlerini alma
print(my_dict.items())  # dict_items([('apple', 1), ('banana', 5), ('orange', 4)])
```

#### split ve join methodu 
```
# Bir stringi boşluklara göre bölmek
sentence = "Python çok güçlü bir dil"
words = sentence.split()
print(words)  # ['Python', 'çok', 'güçlü', 'bir', 'dil']

# Bir stringi farklı bir ayırıcıya göre bölmek
numbers = "1,2,3,4,5"
num_list = numbers.split(',')
print(num_list)  # ['1', '2', '3', '4', '5']
```
```
# Bir liste elemanlarını boşlukla birleştirmek
words = ['Python', 'çok', 'güçlü', 'bir', 'dil']
sentence = ' '.join(words)
print(sentence)  # Python çok güçlü bir dil

# Bir liste elemanlarını farklı bir ayırıcıyla birleştirmek
num_list = ['1', '2', '3', '4', '5']
numbers = ','.join(num_list)
print(numbers)  # 1,2,3,4,5
```

#### list compheransion

new_list = [expression for item in iterable if condition]
```
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4]
```

#### enumerate() Fonksiyonu:
enumerate() fonksiyonu, bir iterable nesnenin indeksini ve değerini döndürür. Bu, bir döngü içinde hem indeks hem de değer ile birlikte çalışmanıza olanak sağlar.
```
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Çıktı:
# 0 apple
# 1 banana
# 2 cherry
```
#### zip fonksiyonu 
zip() fonksiyonu, farklı iterable nesneleri paralel olarak birleştirerek birleştirilmiş bir tuple listesi oluşturur.
```
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

zipped = zip(numbers, letters)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

------------------------------------------------------------------

numbers = [1, 2, 3]
letters = ['a', 'b', 'c', 'd']

zipped = zip(numbers, letters)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

------------------------------------------------------------------
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
symbols = ['!', '@', '#']

zipped = zip(numbers, letters, symbols)
print(list(zipped))  # [(1, 'a', '!'), (2, 'b', '@'), (3, 'c', '#')]

```

#### function 
```
def hello():
    print("Merhaba, dünya!")

hello()  # Fonksiyonu çağırma
```

#### Esnek Sayıda Argümanlar:
```

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3))  # 6
print(add(1, 2, 3, 4, 5))  # 15
```

#### Lambda Fonksiyonları:
```
double = lambda x: x * 2
print(double(5))  # 10
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

### IBM SkillsBuild

```
Konular :
- Sunumunuz için doğru hedefleri belirlemek neden önemlidir?

- Hedef kitlenizi nasıl tanımlarsınız?

- Sunumunuzun yapısını nasıl oluşturursunuz?

- Sunum slaytlarınızı nasıl tasarlıyorsunuz?

- Nasıl daha etkili sunum yaparsınız?

- Sinirlerinizi nasıl yönetirsiniz?

- Beklenmedik durumlarla nasıl başa çıkıyorsunuz?

```

#### Notlar:

- Başarılı bir sunum iki etkene bağlıdır - hazırlık - sunumu yapış

```
  "Sunumunuzda neyi başarmak istediğinizi siz bilmiyorsanız hedef kitleniz hiç bilemez."

– Amerikalı yazar, Harvey Diamond
```
- 1. Sunumunuzun sonucu hakkında net olun
- 2. Sunumunuzun sonucunu belirlemek için işbirliği yapın
- Bilgi edinme, harekete geçme ve hissetme

  <img width="830" alt="Screenshot 2024-04-25 at 22 06 41" src="https://github.com/busecoban/IBM_CyberStart/assets/73944611/974b086a-e010-4913-8273-741130d63631">


Slayt setinizi hedef kitlenize dağıtmalı mısınız? Slayt setleri okumak için değil, sunum yapmak içindir. Bunların paylaşılması, hedef kitlenize aşırı düzeyde bilgi yüklemenize yol açar; bu da sunumunuza olan ilgilerini kaybetmelerine neden olur ve sunum yapan kişi olarak size odaklanmalarını engelleyebilir. Sunumunuzu paylaşmaktan kaçının.

Yapılandırılmış bir sunum, açılış, gelişme ve kapanışı içermelidir; ancak hikaye zorunlu değildir.


 <img width="806" alt="Screenshot 2024-04-25 at 22 17 17" src="https://github.com/busecoban/IBM_CyberStart/assets/73944611/f4f03927-7e08-425f-b19a-c2d8733f9012">

 


```
Düşünce 1: 
"Bir çok politikacı, hedef kitle için neyin en çok işe yarayacağına dair akıllıca bir fikir geliştirmiştir."

– Amerikalı haber spikeri, Jessica Savitch
```
- Düşünce 1: Ne düşünüyorsunuz?

```
Düşünce 2: 
Ekibinizin yeni bir teknoloji türüyle çalışma deneyimi hakkında bir sunum üzerinde çalıştığınızı varsayalım. Sunumu meslektaşlarınıza, ekibinize, müdürünüze veya üst düzey yöneticilerinize yapıyor olsaydınız sunum aynı mı olurdu? Düşüncenizi açıklayın.
```
- Düşünce 2: Ne düşünüyorsunuz?

```
Daha pozitif, samimi ve ilgi çekici görünmek için beden dilinizi nasıl ayarlayabilirsiniz?
```
- Ne düşünüyorsunuz?

#### Etkili sunum teknikleri
  
Sunum sırasında kullanabileceğiniz, aşağıda belirtilenler dahil olmak üzere, birden fazla teknik vardır:

- Anımsatmaya yönelik bir dil kullanma
- Harika hikayeler anlatma
- Fiziksel sahne donanımı veya ayırt edici görsel resimler kullanma
- Hedef kitlenizi tartışmaya dahil etme
- Kontrollü, ancak canlı bir şekilde konuşma ve hareket etme
- İyi sunum yapanların tamamı, bu tekniklerin tümünü olmasa da çoğunu kullanma eğilimi gösterir.

#### Teknik 1: Anımsatıcı bir dil kullanma
Anımsatıcı dili aşağıdakileri yaparak kullanabilirsiniz:
- Şaşırtıcı bilgiler paylaşma
- Kışkırtıcı bir soru sorma
- İnanılmaz bir istatistik paylaşma
- Bir benzetme kullanma
- İlginç veya komik bir hikaye anlatma

Benzetme kullanma
```
Tüm dünya bir sahnedir."

– İngiliz şair, oyun yazarı ve aktör William Shakespeare
```

#### Teknik 2: Harika hikayeler anlatma
```
"Tarih, hikayeler biçiminde öğretilseydi, asla unutulmazdı."

– İngiliz yazar, Rudyard Kipling
```

<img width="803" alt="Screenshot 2024-04-25 at 22 26 14" src="https://github.com/busecoban/IBM_CyberStart/assets/73944611/d15f5b2f-82f9-4dd7-bb89-60c8f32a2a0b">

Harika hikayeler anlatmanın dört adımı
- canlı bir ortam
- ana karakter için bir sorun
- karakterimiz sorunla nasıl mücadele ediyor
- en can alıcı nokta ve sonuç

#### Teknik 3: Fiziksel sahne donanımı veya ayırt edici görsel resimler kullanma
- Steve Jobs'un karton zarfı, sahne donanımına bir örnektir
- Sahne donanımı seçiminize dikkat edin. "Fazla ilginç" olan bir nesne seçerseniz, hedef kitleniz sizi dinlemeyi bırakacaktır.
  
#### Teknik 4: Hedef kitlenizi tartışmaya dahil etme
 hedef kitlenize sorular sorarak veya küçük tartışmalar başlatarak onların ilgisini çekebilirsiniz. Hedef kitle, genellikle soruların sunumun sonunda sorulmasını bekler, ancak sunumun ortasında veya sunum boyunca sorular sorarak onları şaşırtabilirsiniz.
- Hedef kitlenizi izleyicilerden katılımcılara dönüştürebilirsiniz
- Anlatmaktan tartışmaya geçebilirsiniz

#### Teknik 5: Kontrollü, ancak canlı bir şekilde konuşma ve hareket etme
```
"İki tür konuşmacı vardır: gergin olanlar ve yalancılar."

– Amerikalı yazar, Mark Twain
```

<img width="814" alt="Screenshot 2024-04-25 at 22 35 42" src="https://github.com/busecoban/IBM_CyberStart/assets/73944611/553487ab-6810-48a1-8966-471ced9794f1">


 -Soru-Cevap oturumunu ne zaman yapmalısınız?
Çoğu sunum, Soru-Cevap ile sona erme eğilimi gösterir. Bazen bu oturumlar, sunum yapan kişi için sürprizler oluşturabilir. Hedef kitlenin bir üyesinden gelen bir soru sunumunuzun yönünü saptırabilir. İnsanların en son duydukları bilgileri hatırlama eğiliminde oldukları göz önüne alındığında, Soru-Cevap kısmını sona bırakmaktan kaçının. Hedef kitlenin sorulan soruları veya verilen cevapları hatırlamasını istemezsiniz. İdeal olarak, sunumunuzun ana mesajını hatırlamalarını istersiniz veya zihinlerinde bir eylem çağrısı veya benzeri bir ifade uyandırmak isteyebilirsiniz.

Bunu birkaç yolla sağlayabilirsiniz. Örneğin, sunum boyunca Soru-Cevap molaları verebilirsiniz. Bu yöntem, siz ve hedef kitleniz için gerekli olan ve fazlasıyla ihtiyaç duyulan molayı sağlarken, şüpheleri netleştirmenize yardımcı olacaktır. Sonunda Soru-Cevap için biraz zaman ayırmak isteseniz bile bu sorun olmaz. Sunumu belirsiz veya yetersiz biçimde sona erdirmekten kaçınmak için Soru-Cevap bölümünden sonra kapanış yorumlarınızı sunmayı unutmamanız yeterlidir.



### Yazılım Alanlarını Tanıyalım 1 : Siber Güvenlik 

https://www.youtube.com/watch?v=y-xthksY0yY&t=3s




# Hafta 2

### Genel Kültür

#### VCS : version control system
- Git: Git, özellikle açık kaynaklı yazılım projelerinde sıklıkla kullanılan bir VCS aracıdır. Projelerin kaynak kodlarının takip edilmesine ve değişikliklerin yönetilmesine yardımcı olur.

- SVN: SVN (Subversion), bir diğer açık kaynaklı VCS aracıdır. Projelerin tarihçesini yönetir ve farklı sürümleri saklayarak geri dönüşümlü işlemler yapılmasına imkan tanır.

- Mercurial: Mercurial, dağıtık bir VCS aracıdır. Projelerin kaynak kodlarını yönetmek ve farklı sürümlerini saklamak için kullanılır.

### IBM SkillsBuild

### Python

### Clean Code

### Yazılım Alanları Tanıyalım 2: Web Geliştirme
https://www.youtube.com/watch?v=ZCQlk5ZZ30E&t=1s




# Hafta 3

# Hafta 4

# Hafta 5

# Hafta 6


