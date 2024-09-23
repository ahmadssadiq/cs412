from django.shortcuts import render
import random

# List of Muhammad Ali's quotes and corresponding image URLs (hard-coded)
quotes = [
    "Don’t count the days; make the days count.",
    "He who is not courageous enough to take risks will accomplish nothing in life.",
    "Service to others is the rent you pay for your room here on earth.",
]

images = [
    "/static/img/ali1.jpg",  # Replace with actual image path of Muhammad Ali
    "/static/img/ali2.jpg",
    "/static/img/ali3.jpg",
]


def quote(request):
    # Randomly select a quote and an image
    selected_quote = random.choice(quotes)
    selected_image = random.choice(images)

    # Pass the selected quote and image to the template
    context = {"quote": selected_quote, "image": selected_image}
    return render(request, "quote.html", context)


def show_all(request):
    # Pass all quotes and images to the template
    context = {"quotes": quotes, "images": images}
    return render(request, "show_all.html", context)


def about(request):
    return render(request, "about.html")
