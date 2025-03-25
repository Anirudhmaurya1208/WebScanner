from django import forms

class URLScanForm(forms.Form):
    url = forms.URLField(label="Enter a URL to scan", required=True)
