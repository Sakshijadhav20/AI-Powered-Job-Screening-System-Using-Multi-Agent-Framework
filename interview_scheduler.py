# interview_scheduler.py

def generate_interview_email(candidate_name, job_title, match_score):
    email_template = f"""
    Subject: Interview Invitation for {job_title}

    Dear {candidate_name},

    Congratulations! Based on our AI screening, your profile scored {match_score}% match for the position of "{job_title}".

    We would like to invite you for an interview. Please choose a convenient time slot from the following options:
    - Date: April 15, 2025 | Time: 10:00 AM IST
    - Date: April 16, 2025 | Time: 2:00 PM IST
    - Date: April 17, 2025 | Time: 4:00 PM IST

    Interview Format: Google Meet (link will be shared upon confirmation)

    Looking forward to your response.

    Best regards,  
    HR Team
    """
    return email_template
