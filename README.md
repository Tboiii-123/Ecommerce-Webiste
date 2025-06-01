
# 🛒 E-commerce Web Application

A fully functional, responsive **E-commerce platform** built with **Django**, designed with a user-friendly shopping experience in mind. This project includes Autehntication, cart functionality, Stripe checkout, file/media uploads, static/media hosting via CDN and Cloudinary, and professional deployment using Render.


---

## 🚀 Key Features

- 🧾 Product listing & categorization
- 🛍️ Add-to-cart, update & delete functionality
- 🧮 Dynamic cart summary and pricing logic
- 💳 Secure Stripe Checkout integration
- 🔐 User Authentication
- 📤 File & folder uploads (real-time update)
- ☁️ Media files hosted on [Cloudinary](https://cloudinary.com/)
- 🌍 Static files hosted via CDN or external static server
- 🌐 Render-hosted backend (Django)
- 📱 Fully responsive UI (Bootstrap)
- 🔐 Environment variable management for security

---

## 🧰 Tech Stack

| Purpose       | Technology                                      |
|---------------|--------------------------------------------------|
| Backend       | Django (Python)                                 |
| Frontend      | HTML, CSS, Bootstrap, JavaScript                |
| Payments      | Stripe API                                      |
| Media Hosting | Cloudinary                                      |
| Static Hosting| CDN (Render/Cloudflare Pages)                   |
| Deployment    | Render (Backend), Optional: GitHub Pages CDN    |

---

## 📁 Project Structure

```
├── Ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                       # Main eCommerce app
│   ├── templates/
│   ├── static/
│   └── views.py
├── staticfiles/                # Admin static files (served via CDN)
├── media/                      # Media files (hosted on Cloudinary)
├── manage.py
├── requirements.txt
└── README.md

```

---

## ⚙️ Setup Instructions

### 🔧 Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tboiii-123/Ecommerce-Webiste.git
   cd ecommerce-website
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file:

   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   STRIPE_SECRET_KEY=your_stripe_secret_key
   STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run server**
   ```bash
   python manage.py runserver
   ```

---
## 💳 Authentication

- Registration and login forms.
- Session management.
- Profile page .

---

## 💳 Stripe Payment Integration

- Stripe Checkout handles secure payment sessions.
- Environment keys are stored in `.env`.
- Order confirmation page displays after payment is complete.

---

## 📦 Media & Static Files Hosting

### 🌥 Cloudinary for Media Uploads

- Media files (e.g. images, uploaded folders) are automatically stored in Cloudinary.
- Integrated using `cloudinary-storage` backend in Django settings.

### 📡 CDN for Static Files

- Static files collected using:
  ```bash
  python manage.py collectstatic
  ```
- Hosted on Render or any CDN server to serve quickly across the globe.

---

## ☁️ Deployment (Render)

- Python 3.11+ environment setup on Render.
- GitHub connected to Render for CI/CD.
- Environment variables added securely.
- Render pings the site every 10 minutes via GitHub Action to prevent it from sleeping.

---

## 🔄 Real-Time Updates

- Files and folders uploaded appear immediately on the file tree.
- Messages can be read on other devices without refreshing using AJAX (or can be upgraded with WebSockets for full real-time).

---

## 🖼️ Screenshots
> ![ecom](https://github.com/user-attachments/assets/15f866fc-dc76-4d46-9421-d15336c60808)
> ![ecom2](https://github.com/user-attachments/assets/dab3eed4-0d79-4978-a217-ee04437b654b)
 > ![ecom](https://github.com/user-attachments/assets/b70456cd-0f52-4eee-b31c-e99f862be69b)
> ![ecom7](https://github.com/user-attachments/assets/5d235b3c-ff31-4ab4-b1c5-e346b3d306b7)
> ![ecom6](https://github.com/user-attachments/assets/85e9d374-926f-44a0-9b7f-242e0af725dc)
> ![ecom5](https://github.com/user-attachments/assets/28e2183a-00cb-41a7-b40d-a13a3dd2ae2c)
> ![ecom4](https://github.com/user-attachments/assets/4a1bb557-3e73-42af-93f2-9fa499ba47de)
> ![ecom3](https://github.com/user-attachments/assets/b934cb10-2cf7-4072-83a5-baaa9f878bd4)

---

## 🧱 Build Process & Phases

### 📌 Phase 1: Setup

- Django project initialized
- Apps created: `main`

### 🧩 Phase 2: Cart & Checkout

- Cart logic using Django database
- Add/remove/update views
- Stripe integration for checkout

### 🎨 Phase 3: Frontend UI

- Bootstrap used for responsive design
- Font Awesome icons and modals
- File/folder upload with progress feedback

### ☁️ Phase 4: Static/Media Hosting

- Static files hosted via CDN
- Media hosted on Cloudinary

### 🚀 Phase 5: Deployment

- Render deployed backend
- GitHub Actions used to ping server
- CDN and Cloudinary integrated for scalability

---

## 🧪 Testing & Debugging

- Manual testing on multiple screen sizes
- Stripe test cards used
- Logs and Django Debug Toolbar used for backend debugging

---

## 👨‍💻 Author

**Hussein Lawal Taiwo**  
🎓 Python | Django | Web Developer  
📧 lawalhussein775@gmail.com  
📱 +234 9035014430  

---

## 🪪 License

This project is licensed under the MIT License.

---

## 🤝 Contributions

Pull requests and suggestions are welcome!  
Don’t forget to ⭐ this repo if it helped you!
