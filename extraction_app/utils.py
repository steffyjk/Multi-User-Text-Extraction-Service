def send_notification(email):
    from django.core.mail import send_mail
    send_mail(
        'Your Document is Processed',
        'The text extraction process is complete.',
        'steffy.jk2018@gamil.com',
        [email],
    )