from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>HeadHunter API</title>
            </head>
            <body style="font-family: sans-serif; text-align: center; margin-top: 100px;">
                <h1>Здравствуйте еще раз</h1>
                <h2 style="color: #008000;">поставьте фул пж 🙏</h2>
                <p>эндпоинты:</p>

                <div style="margin-top: 30px; text-align: left; width: fit-content; margin-left: auto; margin-right: auto;">
                    <ul style="font-size: 18px; line-height: 1.8;">
                        <li><a href="/api/companies/">Все компании</a></li>
                        <li><a href="/api/companies/1/">Компания с id=1</a></li>
                        <li><a href="/api/companies/1/vacancies/">Вакансии компании с id=1</a></li>
                        <li><a href="/api/vacancies/">Все вакансии</a></li>
                        <li><a href="/api/vacancies/1/">Вакансия с id=1</a></li>
                        <li><a href="/api/vacancies/top_ten/">Топ-10 вакансий по зарплате</a></li>
                        <li><a href="/admin/">Админка</a></li>
                    </ul>
                </div>
            </body>
        </html>
    """)