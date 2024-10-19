from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
import pandas as pd
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
            summary_file = generate_summary(data)  # Generate summary and save to a file
            send_summary_email(summary_file)       # Send email with the attached file
            return HttpResponse("File uploaded and email with summary sent.")
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

def generate_summary(data):
    summary = f"Number of Rows: {len(data)}\n"
    summary += f"Number of Columns: {len(data.columns)}\n"
    summary += f"Column Names: {', '.join(data.columns)}\n"
    summary += f"First 5 Rows:\n{data.head().to_string()}"

    # Save summary to a text file
    with open('summary_report.txt', 'w') as f:
        f.write(summary)

    return 'summary_report.txt'  # Return the path of the summary file

def send_summary_email(summary_file):
    email = EmailMessage(
        'Python Assignment Summary',
        'Please find the attached summary report.',
        'shmansuri86515@gmail.com',  # From email
        ['tech@themedius.ai'],     # To email tech@themedius.ai
    )

    # Attach the generated summary file
    email.attach_file(summary_file)

    email.send()
