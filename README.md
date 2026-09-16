# Locomotive® — L.I.S.A (Locomotive's Interactive Super Assistant) Clone

Duplikat lengkap dan fungsional dari website interaktif **[https://lisa.locomotive.ca/en](https://lisa.locomotive.ca/en)** oleh Locomotive®.

Proyek ini telah di-scrape secara menyeluruh dan direkonstruksi agar dapat dijalankan secara lokal dengan seluruh fitur interaktif, grafis 3D WebGL, animasi tipografi, efek suara, dan percakapan suara (voice narration).

---

## Fitur yang Berhasil Di-Scrap & Dikonfigurasi

1. **Preloader & Brand Intro GSAP**:
   - Animasi scrambler teks interaktif Locomotive (*"Digital-First Agency Based in Montreal, Canada"*).
   - Transisi logo SVG Locomotive yang presisi dengan opsi skip instan via klik.
2. **Avatar 3D WebGL (Three.js & Shaders)**:
   - Model 3D `lisa.glb` (kepala CRT retro, kabel dinamis, turtleneck knitwear).
   - Lingkungan pencahayaan HDR / EXR (`envmap.exr`) untuk refleksi realistik.
   - Layar monitor CRT interaktif dengan terminal teks code matrix (`running_code.mp4`).
   - Cincin 3D dan tekstur studio (`ring.compressed.glb`, `studio_blur_small.jpg`).
3. **Voice Audio & Sound Effects (Web Audio API)**:
   - Backsound ambien `ambient.mp3` dengan loop dan kontrol volume.
   - **319 file suara studio asli** dalam format `.mp3` (`assets/lisa/en/*.mp3`) untuk seluruh variasi dialog percakapan.
   - Visualizer audio interaktif yang merespons frekuensi suara.
4. **Interactive Dialog Tree (100 Langkah)**:
   - Pohon keputusan lengkap tersimpan di `lisa_data.json` dan `index.html`.
   - Flow *"Start a project"* (nama, perusahaan, role, tipe proyek, budget range, deadline, brief upload).
   - Flow *"Join the team"* (lowongan pekerjaan, freelance creative/technical, gif hover preview).
   - Flow *"Drop a quick word"* & *"Discover our culture"*.
5. **Tipografi & Desain Asli**:
   - Webfont resmi: `HelveticaNowDisplay-Regular` dan `PPLocomotiveNew-Light` (.woff2 & .woff).
   - CSS styles asli Locomotive (`main.css`), SVG sprite icons (`sprite.svg`), favicons, dan styling responsif.

---

## Cara Menjalankan

### Cara 1: Menggunakan Python (Direkomendasikan)
Buka terminal di folder ini dan jalankan:
```bash
python server.py --open
```
Server akan berjalan di `http://localhost:3000` dan browser default Anda akan otomatis terbuka.

### Cara 2: Menggunakan NPM
```bash
npm start
```

### Cara 3: Menggunakan Static Server Apa Saja
Anda juga dapat menggunakan server statis lainnya seperti `npx serve`:
```bash
npx serve -p 3000 .
```

---

## Struktur Direktori

```
lisa-locomotive-clone/
│
├── index.html                  # Halaman utama dengan template Vue, Modular config & data dialog
├── lisa_data.json              # Data JSON lengkap seluruh state tree dialog LISA
├── server.py                   # Local server Python dengan MIME types & CORS lengkap
├── package.json                # Script runner untuk npm start
├── README.md                   # Dokumentasi proyek
│
├── assets/
│   ├── 3d/                     # Model 3D cincin, tekstur studio & arkit
│   │   ├── ring.compressed.glb
│   │   ├── studio_blur_small.jpg
│   │   └── arkit.png
│   │
│   ├── fonts/                  # Font resmi Helvetica Now & PP Locomotive New
│   │   ├── HelveticaNowDisplay-Regular.woff2
│   │   ├── HelveticaNowDisplay-Regular.woff
│   │   ├── PPLocomotiveNew-Light.woff2
│   │   └── PPLocomotiveNew-Light.woff
│   │
│   ├── images/                 # Favicons, SVG sprite, dan GIF assets
│   │   ├── sprite.svg
│   │   ├── favicons/
│   │   └── gifs/
│   │
│   ├── lisa/
│   │   ├── fx/
│   │   │   └── ambient.mp3     # Musik latar ambien
│   │   ├── en/                 # 319 file suara voice clip dialog LISA
│   │   │   ├── lisa.intro.1.mp3
│   │   │   ├── lisa.greeting.1.mp3
│   │   │   └── ...
│   │   └── sixty/              # Model 3D avatar LISA & video screen texture
│   │       ├── lisa.glb
│   │       ├── envmap.exr
│   │       ├── running_code.mp4
│   │       ├── idea.mp4
│   │       ├── face1.jpg
│   │       └── face2.jpg
│   │
│   ├── scripts/                # Bundle JavaScript modular Locomotive
│   │   ├── vendors.js
│   │   └── app.js (GSAP, Three.js, Vue 3, HLS.js, Web Audio)
│   │
│   └── styles/
│       └── main.css            # Stylesheet utama Locomotive
│
└── uploads/                    # Job preview GIF & OpenGraph metadata
    ├── job-positions/
    └── metadata/
```

---

## Teknologi & Arsitektur
- **Locomotive Modular JS**: Arsitektur modular berbasis atribut HTML (`data-module-*`).
- **Three.js**: Rendering 3D WebGL untuk karakter avatar LISA dan material PBR shader.
- **GSAP (GreenSock)**: Animasi teks preloader dan transisi state dialog.
- **Vue 3**: Reactive data-binding untuk form, pilihan menu, dan state management percakapan.
- **Web Audio API**: Pemutaran audio suara asisten dan audio reactive visualizer.
