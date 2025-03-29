import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
import threading

def generate_qr():
    text = entry.get()
    if not text:
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img = img.resize((200, 200))
    
    qr_image = ImageTk.PhotoImage(img)
    qr_canvas.create_image(0, 0, anchor='nw', image=qr_image)
    qr_canvas.image = qr_image

def on_generate_press():
    threading.Thread(target=generate_qr).start()

app = ctk.CTk()
app.geometry("400x400")
app.title("QR Gen")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app.configure(bg="#121212")

entry = ctk.CTkEntry(app, width=320, height=40, placeholder_text="Enter text here", corner_radius=15, fg_color="#1F1B24", text_color="white")
entry.pack(pady=20)

generate_button = ctk.CTkButton(app, text="Generate QR Code", corner_radius=10, fg_color="#BB86FC", text_color="black", hover_color="#3700B3", command=on_generate_press)
generate_button.pack(pady=10)

qr_canvas = ctk.CTkCanvas(app, width=200, height=200, bg="white", highlightthickness=0)
qr_canvas.pack(pady=20)

app.mainloop()
