# 雅 UDON - Professional Udon Noodles Website

A sleek, professional website for selling authentic Japanese udon noodles.

## Features

- **Home Page**: Displays 6 different udon products with pricing and descriptions
- **Contact Page**: Shows business email and social media links
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Professional Styling**: Modern, clean design with smooth animations
- **Interactive Elements**: Hover effects, smooth scrolling, and order buttons

## Setup Instructions

1. **Add Your Images**: Create an `images` folder in the same directory as the HTML files and add the following images:
   - `hero-bg.jpg` - Background for the home page hero section (recommended: 1920x600px)
   - `contact-bg.jpg` - Background for contact page hero (recommended: 1920x600px)
   - `kake-udon.jpg` - Kake Udon product image
   - `tempura-udon.jpg` - Tempura Udon product image
   - `curry-udon.jpg` - Curry Udon product image
   - `nabeyaki-udon.jpg` - Nabeyaki Udon product image
   - `yaki-udon.jpg` - Yaki Udon product image
   - `zaru-udon.jpg` - Zaru Udon product image

   Recommended size for product images: 800x600px or similar aspect ratio

2. **Update Contact Information**: Edit `contact.html` to add your actual:
   - Email address (replace `orders@miyabiudon.com`)
   - Social media links (Instagram, Facebook, Twitter)
   - Business hours

3. **Customize Content**:
   - Update product names, descriptions, and prices in `index.html`
   - Modify the business name and branding as needed
   - Adjust color scheme in `styles.css` (see CSS variables at the top)

## File Structure

```
udon-noodles/
├── index.html          # Home page with products
├── contact.html        # Contact page
├── styles.css          # All styling
├── script.js           # JavaScript for interactions
├── README.md           # This file
└── images/            # Folder for all images (you need to create this)
    ├── hero-bg.jpg
    ├── contact-bg.jpg
    ├── kake-udon.jpg
    ├── tempura-udon.jpg
    ├── curry-udon.jpg
    ├── nabeyaki-udon.jpg
    ├── yaki-udon.jpg
    └── zaru-udon.jpg
```

## Quick Start

1. Download or find high-quality udon images online
2. Place them in the `images/` folder
3. Open `index.html` in a web browser
4. Test on mobile by resizing your browser window

## Features Breakdown

### Home Page
- Eye-catching hero section with your brand name
- Grid of 6 udon products with:
  - Product images
  - Names and descriptions
  - Pricing
  - Order buttons (email links)
  - Special badges (Popular, Best Seller, etc.)
- "Why Choose Us" section highlighting your strengths

### Contact Page
- Professional contact information display
- Email link for easy ordering
- Social media buttons for Instagram, Facebook, and Twitter
- Business hours clearly displayed
- Call-to-action section for placing orders

### Responsive Design
- Mobile-friendly navigation
- Adaptive grid layouts
- Optimized for all screen sizes

## Customization Tips

### Colors
Edit the CSS variables in `styles.css` (lines 9-17) to match your brand:
```css
:root {
    --primary-color: #2c3e50;      /* Main dark color */
    --secondary-color: #c9a961;    /* Secondary gold */
    --accent-color: #d4af37;       /* Accent gold */
    /* ... */
}
```

### Products
Add or remove products by copying the `.product-card` div structure in `index.html`

### Fonts
The site uses Google Fonts (Playfair Display and Inter). Change them in the `<head>` section of both HTML files.

## Browser Compatibility

Works on all modern browsers:
- Chrome/Edge
- Firefox
- Safari
- Mobile browsers

## License

This is your business website - use it however you need!

---

**Need help?** Make sure all files are in the same directory and the images folder is created with your product photos.
