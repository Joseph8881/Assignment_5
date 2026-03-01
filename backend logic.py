from django.shortcuts import render
from .forms import PuzzleForm
import math
import random

def puzzle_view(request):
    result = None

    if request.method == "POST":
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
            text = form.cleaned_data["text"]

            # -------------------
            # Number Puzzle
            # -------------------
            if number % 2 == 0:
                number_result = f"{number} is Even. Square root: {math.sqrt(number)}"
            else:
                number_result = f"{number} is Odd. Cube: {number ** 3}"

            # -------------------
            # Text Puzzle
            # -------------------
            binary_text = ' '.join(format(ord(char), '08b') for char in text)

            vowels = "aeiouAEIOU"
            vowel_count = sum(1 for char in text if char in vowels)

            text_result = f"Binary: {binary_text} | Vowel Count: {vowel_count}"

            # -------------------
            # Treasure Hunt Simulation
            # -------------------
            secret_number = random.randint(1, 100)
            attempts = 0
            success = False

            while attempts < 5:
                guess = random.randint(1, 100)
                attempts += 1
                if guess == secret_number:
                    success = True
                    break

            if success:
                treasure_result = f"You won! Guessed in {attempts} tries."
            else:
                treasure_result = "You lost! Could not guess in 5 tries."

            result = {
                "number_result": number_result,
                "text_result": text_result,
                "treasure_result": treasure_result
            }
    else:
        form = PuzzleForm()

    return render(request, "puzzle/result.html", {
        "form": form,
        "result": result
    })