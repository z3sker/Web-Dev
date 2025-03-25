from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Online Shop</title>
            </head>
            <body style="text-align: center; font-family: sans-serif; margin-top: 100px;">
                <h1>Здравствуйте 👋</h1>
                <h2 style="color: green;">плиз поставьте фул 🙏</h2>
            </body>
        </html>
    """)