from django.shortcuts import render
import random

# List of quotes and corresponding image URLs (hard-coded)
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Do not watch the clock; do what it does. Keep going.",
]

images = [
    "/static/img/person1.jpg",  # Replace with actual image path
    "/static/img/person2.jpg",
    "/static/img/person3.jpg",
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
