# Welcome to Yoshelin Inventory
Generated by...

Nama    :   Yoshelin Yamala Vijnana

Kelas   :   PBP B

NPM     :   2206826702

Tautan repository Adaptable: (already disabled...)

# =====================================
# ₊✧ Tugas 1 PBP ₊✧
# =====================================
# Implementasi Checklist Step by Step
# 1.  Checklist 1:  Membuat sebuah proyek Django baru.
Django adalah sebuah framework website yang bersifat open source dalam Python yang tujuannya untuk web developing secara efisien dan aman.

- Untuk membuat proyek Django baru, step pertama yang perlu dilakukan adalah mengaktifkan virtual environment. Pengaktifan virtual environment dapat dilakukan dengan cara memasukkan perintah ini pada terminal:
  
            ```python -m venv env`

- Kemudian, untuk memunculkan (env) pada terminal, kita perlu memasukkan: 

            `env\Scripts\activate.bat`

pada command prompt, kemunculan (env) menjadi tanda bahwa virtual environment sudah aktif.

- Langkah selanjutnya yang perlu dilakukan ialah menyiapkan dependencies. Dependencies dapat memastikan bahwa program atau proyek tertentu dapat berjalan tanpa kesalahan. Di dalam direktori, saya membuat `requirements.txt`` yang berisi:

  ```
        python
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3 
        
   ```
- Dependencies kemudian di install dengan menjalankan perintah ini pada terminal:

            `pip install -r requirements.txt`
        
 - Kemudian saya membuat proyek Django baru dengan nama `mysite` dengan menjalankan perintah berikut:

            `pip install django`

            `django-admin startproject mysite .`

- Pada settings.py, kita perlu menambahkan `"*"` pada `ALLOWED_HOST` untuk mengubah pengaturan akses.
- Menambahkan berkas `.gitignore`
- Tambahkan `'main'`` ke INSTALLED_APPS di settings.py
- Cek apakah Django telah berhasil dibuat, dengan cara memasukkan perintah berikut pada direktori:

            `python manage.py runserver`

 kemudian klik tautan <http://localhost:8000> pada peramban anda.

# 2. Checklist 2: Membuat aplikasi dengan nama main pada proyek tersebut.
- Buatlah main didalam project yoshe.business menggunakan manage.py menggunakan perintah 
        
        `python manage.py startapp main`

- Ketika berhasil dijalankan, main akan terbentuk dalam direktori. Selanjutnya kita perlu add folder `templates` yang berisi `main.html`
- Kemudian kita tambahkan `main` ke INSTALLED_APPS di settings.py
  
    
# 3. Checklist 3: Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
 - Pertama tama, kita perlu setup `urls.py` di app `main` dengan mengisi

   ```
        from django.urls import path
        from main.views import show_main
        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
   ```


- Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main
     
  ```
             urlpatterns = [
            ...
            path('main/', include('main.urls')),
            ...
          ]
          
  ```
     
# 4. Checklist 4: Membuat model pada aplikasi main dengan nama `Item`` dan memiliki atribut wajib
- Melakukan setup pada `item` sesuai dengan ketentuan soal, pada atribut `nama, amount, date_added, price, description`
- Selanjutnya lakukan run 
            
            `./manage.py makemigrations` 
            
     dan 

            `./manage.py migrate` 
            
     untuk me-migrasikan ke database.

# 5. Checklist 5:  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
- Setup views.py dengan melakukan inisiasi data yang akan dipanggil pada main, kemudian buat juga render html nya sebagai berikut:

            `render(request, "main.html", context)` 

- Pada main, kita lakukan `include` pada root project, yakni file `urls.py`

# 6. Checklist 6: Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Lakukan `add, commit, dan push` ke GitHub dan lakukan deployment pada platform Adaptable sesuai dengan perintah yang tersedia pada Tutorial 0 PBP.



# Bagan yang berisi request client ke web aplikasi berbasis Django
![Bagan_Django_Yoshelin](https://github.com/yoshelinn/yoshe.business/assets/120077685/081f0139-bc81-4284-8db7-27e577b68356)

 - Keterkaitan antara urls.py dan views.py adalah bahwa urls.py berfungsi untuk menguraikan argumen dari URL dan meneruskannya ke views.py yang sesuai. Setelah itu, views.py akan mengambil permintaan tersebut dan menghasilkan respons web yang sesuai.

 - Hubungan antara views.py dan berkas HTML adalah bahwa views.py akan mengambil template dari berkas HTML. Selanjutnya, template tersebut akan digabungkan dan diproses oleh views.py sehingga menghasilkan halaman web yang lengkap.

 - Kaitan antara views.py dan models.py terletak pada fakta bahwa models.py akan mengambil data dari database dan mengirimkannya ke views.py.

- Secara keseluruhan, urls.py berfungsi untuk mengelola argumen yang diterima dari pengguna dan mengarahkannya ke berkas HTML yang berisi template web. Berkas HTML tersebut akan menghasilkan outputnya melalui views.py. Ketika ada permintaan untuk mengambil data, models.py berperan sebagai perantara yang menghubungkan views.py dengan database. Dengan demikian, views.py dapat menggabungkan dan memproses data tersebut untuk menciptakan halaman web yang utuh.


# Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

 - Virtual Environment (VE) adalah alat yang membantu pengembang perangkat lunak mengisolasi proyek mereka dari yang lain, sehingga setiap proyek dapat memiliki dependensi yang berbeda tanpa saling mengganggu. Hal ini memungkinkan penggunaan versi yang berbeda dari modul yang sama dalam setiap proyek, dan VE memiliki beberapa manfaat penting:
        1. Isolasi Dependensi: VE memungkinkan proyek-proyek berbeda untuk memiliki dependensi yang berbeda, seperti versi modul yang berbeda, tanpa konflik.
        2. Manajemen Dependensi yang Jelas: VE membantu mengelola dan menjaga daftar dependensi yang jelas untuk setiap proyek, menghindari kebingungan dan penghapusan yang tidak sengaja.
        3. Menghindari Konflik Dependensi: VE mencegah konflik antara dependensi yang berbeda, memastikan bahwa proyek-proyek berjalan dengan lancar.

- Meskipun memungkinkan dengan tidak menggunakan VE, disarankan untuk menggunakan lingkungan virtual saat membuat aplikasi web berbasis Django. Hal ini bertujuan agar versi perpustakaan (library) yang digunakan dalam satu proyek tidak terpengaruh jika kita melakukan pembaruan pada perpustakaan yang sama dalam proyek lainnya.


# Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Model-View-Controller (MVC), Model-View-Template (MVT), dan Model-View-ViewModel (MVVM) adalah arsitektur desain perangkat lunak yang digunakan dalam pengembangan aplikasi. 

- MVC (Model-View-Controller):
Model: Mengelola data dan logika bisnis aplikasi. Ini berinteraksi dengan database dan mengambil, memodifikasi, atau menyimpan data.
        View: Bertanggung jawab untuk menampilkan data kepada pengguna dalam bentuk yang sesuai. Ini tidak berisi logika bisnis tetapi hanya menampilkan informasi.
        Controller: Bertindak sebagai perantara antara Model dan View. Ini mengontrol alur aplikasi, mengelola permintaan pengguna, dan mengatur interaksi antara Model dan View. Ini juga menangani routing dan pengolahan permintaan.

- MVT (Model-View-Template):
Model: Mirip dengan MVC, Model mengelola data dan logika bisnis. Ini berhubungan dengan database dan operasi data lainnya.
        View: View dalam MVT adalah logika yang mengatur cara tampilan akan ditampilkan kepada pengguna, mirip dengan template dalam MVC.
        Template: Bertanggung jawab untuk rendering tampilan yang disesuaikan dengan data yang diberikan oleh View. Template ini menentukan cara tampilan akhir akan muncul.

-  MVVM (Model-View-ViewModel):
Model: Seperti dalam MVC dan MVT, Model mengelola data dan logika bisnis aplikasi.
        View: Bertanggung jawab untuk menampilkan data dan interaksi dengan pengguna seperti dalam MVC.
        ViewModel: Ini adalah bagian yang paling khas dari MVVM. ViewModel menghubungkan Model dan View. Ini menangani logika tampilan dan transformasi data sehingga dapat ditampilkan dengan benar di View. ViewModel berperan sebagai perantara antara Model dan View.

- Perbedaan utama antara ketiganya adalah:
1. Template vs. View vs. Controller/ViewModel: MVC memiliki View, MVT memiliki Template, dan MVVM memiliki View dan ViewModel. MVVM memiliki ViewModel tambahan yang mengelola logika tampilan.
2. Penanganan Logika Tampilan: MVC dan MVT memiliki logika tampilan dalam Controller dan Template masing-masing, sementara MVVM memisahkan logika tampilan ke dalam ViewModel yang terpisah.
3. Struktur Pengembangan: Struktur MVC lebih berfokus pada kontrol alur aplikasi, sedangkan MVT lebih berfokus pada tampilan yang dihasilkan dari Template. MVVM menambahkan abstraksi tambahan untuk mengelola tampilan dengan baik.


# ============================================
# ₊✧ Tugas 2 PBP ₊✧
# ============================================

# 1. Checklist 1: Apa perbedaan antara form POST dan form GET dalam Django?
Dalam Django, kita dapat menggunakan metode POST dan GET untuk mengirim data dari formulir HTML ke server web Django.

- Aspek Delivery Data
Dalam form POST, input data yang dimasukkan ke form akan dikirim ke dalam server web sebagai body request dari HTTP. Data bersifat invisible. 

Dalam form GET, data yang dikirim ke form merupakan bagian dari URL sehingga data terlihat dalam alamat website. Data bersifat visible.

- Aspek Security
Form POST lebih aman karena data yang di-deliver tidak terlihat dalam URL, sehingga tidak mudah terpapar ke publik,

Form GET tingkat keamanannya lebih rendah dari form POST karena data nya bersifat visible, maka data dapat dilihat oleh pengguna lain.

- Aspek Kapasitas
Form POST memiliki batasan ukuran data yang dapat di-deliver lebih besar dibandingkan degan form GET.

# 2. Checklist 2: Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Perbedaan dapat dilihat di tabel berikut ini:
![Perbedaan](https://github.com/yoshelinn/yoshe.business/assets/120077685/31b5367b-98aa-4d0a-997b-461574eee259)


# 3. Checklist 3: Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
**1.** Format JSON readable sehingga mudah dimengerti

**2.** Compatible dengan banyak bahasa pemrograman

**3.** Format data yang digunakan JSON merupakan format data umum dalam API, untuk mengirim permintaan dan menerima respons.

**4.** Pertukaran data antar server dan klien aman

# 4. Checklist 4: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 

**1. Membuat input form untuk menambahkan objek model pada app sebelumnya.**
- Pertama tama, buat `base.html` pada template yang ada di root
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>```

- Kemudian, kita add `settings.py` dengan kode agar base.html dapat dideteksi sebagai templates
```TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
```

- Pada `forms.py` kita mengimpor `ModelForm` dan Item yang berisi fields, yang bertujuan untuk menambah item ke database dengan `ModelForm`

  ```
         from django.forms import ModelForm
         from main.models import Item

          class ProductForm(ModelForm):
           class Meta:
           model = Item
           fields = ["name", "amount", "description", "price" ]
  ```

- Pada `templates > create_product.html`, 
berisi fungsi `create_product(request)` yang dapat mengakses file `create_product.html` untuk menerima request, membuat dan menyimpan data yang diinput pada form.
 ```
from django.http import HttpResponse
    from django.core import serializers
    from django.shortcuts import render
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    from main.models import Item
    from django.forms import ModelForm

def show_main(request):
    items = Item.objects.all()
    item_count = items.count()

    context = {
        'name': 'Yoshelin Yamala Vijnana',
        'class': 'PBP B',
        'items': items,
        'item_count': item_count,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```


- Memodifikasi `urls.py` dengan add `create_product`
    ```from main.views import *
    from django.urls import path
from main.views import *
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
]
...
```

**- Dengan form yang sudah ada, maka itu dapat menjadi bekal untuk melengkapi `create_product.html` dan `main` sebagai berikut:**
```
{% extends 'base.html' %}

{% block content %}
<style>
    body {
        background-color: #abd3cc;
    }
</style>

<h1 style="color: #00a99d; font-size: 34px;">Selamat Datang di Yoshelin Inventory</h1>
<p>By: Yoshelin | PBP B | 2206826702 <p>

<hr style="border: 1px solid #00a99d ">

<p>     </p>  
<h5> Nama:  </h5>
<p>{{ name }}</p>


<h5> Kelas: </h5>
<p>{{ class }}</p>


<h5> Produk: </h5>
<p>{{ item }}</p>

<p>Kamu telah menyimpan {{ items|length }} item pada aplikasi ini.</p>

<style>
    table {
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 3px solid #00a99d;
        text-align: left;
        padding: 10px;
    }

    th {
        background-color: #00a99d;
    }
</style>

<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Amount</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>
    {% for item in items %}
        <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.amount }}</td>
            <td>{{ item.description }}</td>
            <td>{{ item.date_added }}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Item
    </button>
</a>

<style>
    h5 {
        font-size: 18px;
    }

    p {
        font-size: 16px;
    }
</style>

{% endblock content %}
```

(Saya menambahkan tabel, garis horizontal dan pemberian warna background pada Inventory App saya.)

**2.  Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.**

- Untuk melihat objek dengan format tersebut, langkah pertama yang harus kita lakukan yakni dengan melakukan import di `views.py`
  ```
  from django.http import HttpResponse
  from django.core import serializers
  ```

- Kemudian, kita bisa langsung menginisiasi fungsi untuk menampilkan format HTML, XML, JSON. XML by ID, dan JSON by ID. Sebagai berikut: (pada views.py)
```
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.forms import ModelForm

def show_main(request):
    items = Item.objects.all()
    item_count = items.count()

    context = {
        'name': 'Yoshelin Yamala Vijnana',
        'class': 'PBP B',
        'items': items,
        'item_count': item_count,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

**3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**

- Import semua fungsi yang telah dibuat pada `views.py` di direktori main, kemudian tambahkan semua path sesuai dengan fungsi yang telah dibuat sebagai berikut:
```
from django.urls import path
from main.views import *
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ]

```

# Mengakses kelima URL di poin 2 menggunakan Postman
# 1. HTML
![html1](https://github.com/yoshelinn/yoshe.business/assets/120077685/c0d359bd-e473-4dd8-ae8c-22f5aa9e6bd9)
![html2](https://github.com/yoshelinn/yoshe.business/assets/120077685/9cc5ec14-c9b5-43d3-a1d8-6882d005677f)
![html3](https://github.com/yoshelinn/yoshe.business/assets/120077685/3daad420-29c9-4f1a-a41e-60a7f8c7ec10)
![html4](https://github.com/yoshelinn/yoshe.business/assets/120077685/229d02c4-d861-4687-918e-fa690f82f5a8)
![html5](https://github.com/yoshelinn/yoshe.business/assets/120077685/f31fc3a3-a9db-4a2d-9e0c-cc9964023a1a)


# 2. XML
![xml1yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/f0c350c8-5250-4568-8314-ec6ffe1cfdaf)
![xml2yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/0fb20cee-63b8-419f-96bb-cb077909ae9b)

# 3. JSON
![json1yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/5d29980c-93f6-4268-9311-2db71be0e9ba)
![json2yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/38bd6a56-7136-41f3-ac74-7e7c1a9fa5ce)
![json3yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/82570a15-9d66-4f12-a250-93f1fcd4519b)

# 4. XML by ID
![xmlbyid1yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/3649dedf-277f-4a35-9cfc-16ecad794bc1)
![xmlbyid2yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/25efd542-5fb8-4de3-92be-6949c5fd6a61)
![xmlbyid3yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/4977a7fe-6c9e-4415-a41f-ade1914a73eb)
![xmlbyid4yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/6eec57ea-f6a2-4138-8def-9adbae50c9db)

# 5. JSON by ID
![jsonbyid1yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/69b12ef8-860a-4004-8d48-900a935c293d)
![jsonbyid2yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/3daf6f10-a36d-480c-b412-4ac108c2f2b2)
![jsonbyid3yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/eea3e6ee-d4ca-4ba8-a831-e7569e100dd4)
![jsonbyid4yoshe](https://github.com/yoshelinn/yoshe.business/assets/120077685/16a9f309-881b-4130-8c44-918bf6743478)

