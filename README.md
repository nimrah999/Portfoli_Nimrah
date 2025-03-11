# Portfolio Website - Nimrah Khan

A minimalist portfolio website showcasing expertise in instructional design and VR/AR learning, built with Flask.

## Features

- Clean, minimalist design
- Responsive layout
- Smooth animations
- Sections for About, Work, Projects, Insights, and Contact

## Tech Stack

- Flask (Python web framework)
- HTML5
- CSS3
- JavaScript (Vanilla)
- Font Awesome for icons
- Google Fonts (Inter)

## Local Development

1. Clone the repository
```bash
git clone [your-repo-url]
cd [repo-name]
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python main.py
```

The application will be available at `http://localhost:5000`

## Deployment

### GitHub Repository Setup

1. Create a new repository on GitHub
2. Initialize Git in your local project:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin [your-github-repo-url]
git push -u origin main
```

### Deployment Platforms

The project is configured to be deployed on various platforms:

- **Heroku**: Ready to deploy with included Procfile
- **Vercel**: Compatible with Python/Flask deployments
- **DigitalOcean App Platform**: Ready for deployment

## Project Structure

```
.
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
├── app.py
├── main.py
├── Procfile
└── requirements.txt
```

## License

All rights reserved.