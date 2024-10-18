from django.shortcuts import render

# Create your views here.
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

from django.shortcuts import render
from .forms import TransactionForm
import numpy as np

def generate_features():
    """Generate random values for anonymized features."""
    return np.random.normal(0, 1, 28)  # Assuming 28 features with normal distribution

def index(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            time = form.cleaned_data['time']

            # Generate the anonymized features
            v_features = generate_features()

            # Prepare input data
            input_data = np.append(v_features, [amount, time]).reshape(1, -1)

            # Make a prediction
            prediction = model.predict(input_data)[0]
            message = "Fraud detected!" if prediction == 1 else "No fraud detected."
            return render(request, 'result.html', {'message': message})
    else:
        form = TransactionForm()
    return render(request, 'index.html')