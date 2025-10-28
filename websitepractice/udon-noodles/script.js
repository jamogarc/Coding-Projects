// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe product cards
document.addEventListener('DOMContentLoaded', () => {
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });

    const features = document.querySelectorAll('.feature');
    features.forEach((feature, index) => {
        feature.style.opacity = '0';
        feature.style.transform = 'translateY(30px)';
        feature.style.transition = `opacity 0.6s ease ${index * 0.15}s, transform 0.6s ease ${index * 0.15}s`;
        observer.observe(feature);
    });

    const contactCards = document.querySelectorAll('.contact-card');
    contactCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.15}s, transform 0.6s ease ${index * 0.15}s`;
        observer.observe(card);
    });
});

// Order button functionality
document.querySelectorAll('.order-btn').forEach(button => {
    button.addEventListener('click', function(e) {
        const productCard = this.closest('.product-card');
        if (productCard) {
            const productName = productCard.querySelector('h3').textContent;
            const productPrice = productCard.querySelector('.price').textContent;

            // Create email link with pre-filled content
            const subject = encodeURIComponent(`Order: ${productName}`);
            const body = encodeURIComponent(`Hi, I would like to order:\n\nProduct: ${productName}\nPrice: ${productPrice}\n\nPlease let me know about availability and delivery options.\n\nThank you!`);

            window.location.href = `mailto:orders@miyabiudon.com?subject=${subject}&body=${body}`;
        }
    });
});

// Mobile menu toggle (for future enhancement)
const navToggle = document.querySelector('.nav-toggle');
if (navToggle) {
    navToggle.addEventListener('click', () => {
        document.querySelector('.nav-links').classList.toggle('active');
    });
}
