from flask import Flask, render_template, url_for,jsonify, request
import stripe

app = Flask(__name__)

app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51IEVmzBlXlBcSlHqZGlZKIO3x9L39zAJEN7mD6GrkfztKrQmPhbfhoqqltk2DjRTCaGKhKlmvk1wKh9xuAr5mIRi008MjWppj0'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51IEVmzBlXlBcSlHqYzUWcPYOYjiRHMPHn0Dr0miFYjOCsIsy7zzypL3ZGUBPrm9ds1lGwYfkw1fyaar6bpbFMHgC00wCbY9Ifs'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/')
def create_checkout_session():
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': 20,
                    'product_data': {
                        'name': 'Stubborn Attachments',
                        'images': ['https://i.imgur.com/EHyR2nP.png'],
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=url_for('Thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',  #YOUR_DOMAIN + '/success.html',
        cancel_url= url_for('index', _external=True),                                         # YOUR_DOMAIN + '/cancel.html',
    )
    return render_template(
        'index.html',
        checkout_session_id = session['id'],
        checkout_session_key= app.config['STRIPE_PUBLIC_KEY']
    )

if __name__ == '__main__':
    app.run(debug=True)
