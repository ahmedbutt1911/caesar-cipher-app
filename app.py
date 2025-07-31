from flask import Flask, render_template, request

app = Flask(__name__)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def encryption(msg, shift):
    cipher_text = ""
    for char in msg:
        if char in alphabet:
            result = (alphabet.index(char) + shift) % 26
            cipher_text += alphabet[result]
        else:
            cipher_text += char
    return cipher_text

def decryption(cipher_text, shift):
    original_text = ""
    for char in cipher_text:
        if char in alphabet:
            result = (alphabet.index(char) - shift) % 26
            original_text += alphabet[result]
        else:
            original_text += char
    return original_text

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        direction = request.form.get("direction")
        msg = request.form.get("message", "").lower()
        try:
            shift = int(request.form.get("shift", 0))
        except ValueError:
            shift = 0

        if direction == "encode":
            result = encryption(msg, shift)
        elif direction == "decode":
            result = decryption(msg, shift)
        else:
            result = "Invalid option selected."
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
