# Payment_Method-Python-Flask-Stripe

from flask import Flask, jsonify, request
import stripe

stripe.api_key = 'sk_test_51IEVmzBlXlBcSlHqYzUWcPYOYjiRHMPHn0Dr0miFYjOCsIsy7zzypL3ZGUBPrm9ds1fyaar6bpbFMHgC00wCbY9Ifs'
app = Flask(__name__,
            static_url_path='',
            static_folder='.')
YOUR_DOMAIN = 'http://localhost:4242'
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(port=4242)

###############################################################################
# For RUNNING Application  use :  http://localhost:4242/checkout.html
#  Use card number as :  4242 4242 4242 4242
