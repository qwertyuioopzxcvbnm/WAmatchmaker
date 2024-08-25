import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import warnings
import os


warnings.simplefilter("ignore", FutureWarning)

data = pd.read_csv('file.csv')
data = pd.DataFrame(data)

def sendResults(ind, num):
    distributor = "xanderdshotz@gmail.com"
    password = "uqix ojwk oery vapa"  

    
    match_results_html = ""
    for i in range(1, 6):
        person = data.iloc[ind[i][0]]
        match_results_html += f"""
        <tr>
            <td><strong>{person[2]}</strong></td>
            <td>{ind[i][1]}% match</td>
            <td>snapchat: {person[3]}</td>
            <td>instagram: {person[4]}</td>
            <td>tiktok: {person[5]}</td>
        </tr>
        """

    
    gif_path = "love.gif"
    with open(gif_path, "rb") as f:
        gif_data = f.read()

    
    msg = MIMEMultipart()
    msg['Subject'] = "Butterknife Matchmaker Survey Results!!"
    msg['From'] = distributor
    msg['To'] = ind[0]

    # Add the GIF to the email as an inline image
    gif_cid = f"gif_{os.path.basename(gif_path)}"
    part_gif = MIMEImage(gif_data, name=os.path.basename(gif_path))
    part_gif.add_header("Content-ID", f"<{gif_cid}>")
    msg.attach(part_gif)

   
    body = f"""
    <html>
      <head>
        <style>
          body {{ font-family: Arial, sans-serif; }}
          table {{ width: 100%; border-collapse: collapse; }}
          td, th {{ border: 1px solid #dddddd; text-align: left; padding: 8px; }}
          th {{ background-color: #ffcccb; }}
        </style>
      </head>
      <body>
        <img src="cid:{gif_cid}" alt="love" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">
        <h2 style="text-align: center;">Your Butterknife Matchmaker Results</h2>
        <p style="text-align: center;">Courtesy of Avy Agrawal and Xander Shotz</p>
        <table>
          <tr>
            <th>Name</th>
            <th>Match Percentage</th>
            <th>Snapchat</th>
            <th>Instagram</th>
            <th>TikTok</th>
          </tr>
          {match_results_html}
        </table>
      </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))

    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(distributor, password)
    server.sendmail(distributor, ind[0], msg.as_string())
    server.quit()
    num+=1
    return num

