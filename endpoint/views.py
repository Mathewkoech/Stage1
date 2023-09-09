from django.shortcuts import render
import os
import datetime
import json
from django import views

class EndpointView(views.View):
  def get(self, request, slack_name,Response ,track):
    # Get the required information.
    current_day_of_week = datetime.datetime.utcnow().weekday()
    current_utc_time = datetime.datetime.utcnow()
    github_url_of_file_being_run = os.environ['GITHUB_URL_OF_FILE_BEING_RUN']
    github_url_of_full_source_code = os.environ['GITHUB_URL_OF_FULL_SOURCE_CODE']

    # Validate the UTC time.
    if current_utc_time.hour < (current_utc_time.hour - 2) or current_utc_time.hour > (current_utc_time.hour + 2):
      return Response({
        "status_code": 400,
        "message": "The UTC time is outside the +/-2 hour tolerance."
      })

    # Create the JSON response.
    response = {
      "slack_name": 'HNGx',
      "current_day_of_week": current_day_of_week,
      "current_utc_time": current_utc_time,
      "track": 'Backend',
      "GitHub URL of the file being run": github_url_of_file_being_run,
      "GitHub URL of the full source code": github_url_of_full_source_code,
      "status_code": 200
    }

    return Response(response)
