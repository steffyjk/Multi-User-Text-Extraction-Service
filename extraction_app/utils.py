def send_notification(email, data):
    from django.core.mail import send_mail
    send_mail(
        'Your Document is Processed',
        f'The text extraction process is complete.{data}',
        'steffy.jk2018@gamil.com',
        [email],
    )