from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.platypus.flowables import Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfdoc
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont

# Import our font
registerFont(TTFont('Inconsolata', 'fonts/Inconsolata-Regular.ttf'))
registerFont(TTFont('InconsolataBold', 'fonts/Inconsolata-Bold.ttf'))
registerFontFamily('Inconsolata', normal='Inconsolata', bold='InconsolataBold')

# Set the page height and width
HEIGHT = 11 * inch
WIDTH = 8.5 * inch

# Set our styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Content',
                          fontFamily='Inconsolata',
                          fontSize=8,
                          spaceAfter=.1*inch))
                            


def generate_print_pdf(data, contact):
    pdfname = 'resume.pdf'
    doc = SimpleDocTemplate(
        pdfname,
        pagesize=letter,
        bottomMargin=.5 * inch,
        topMargin=.7 * inch,
        rightMargin=.4 * inch,
        leftMargin=.4 * inch)  # set the doc template
    style = styles["Normal"]  # set the style to normal
    story = []  # create a blank story to tell
    contentTable = Table(
        data,
        colWidths=[
            0.8 * inch,
            6.9 * inch])
    tblStyle = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONT', (0, 0), (-1, -1), 'Inconsolata'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT')])
    contentTable.setStyle(tblStyle)
    story.append(contentTable)
    doc.build(
        story,
        onFirstPage=myPageWrapper(
            contact)
        )
    return pdfname


"""
    Draw the framework for the first page,
    pass in contact info as a dictionary
"""
def myPageWrapper(contact):
    # template for static, non-flowables, on the first page
    # draws all of the contact information at the top of the page
    def myPage(canvas, doc):
        canvas.saveState()  # save the current state
        canvas.setFont('InconsolataBold', 16)  # set the font for the name
        canvas.drawString(
            .4 * inch,
            HEIGHT - (.4 * inch),
            contact['name'])  # draw the name on top left page 1
        canvas.setFont('Inconsolata', 8)  # sets the font for contact
        canvas.drawRightString(
            WIDTH - (.4 * inch),
            HEIGHT - (.4 * inch),
            contact['website'])  
        canvas.line(.4 * inch, HEIGHT - (.47 * inch), 
            WIDTH - (.4 * inch), HEIGHT - (.47 * inch))
        canvas.drawString(
            .4 * inch,
            HEIGHT - (.6 * inch),
            contact['phone'])
        canvas.drawCentredString(
			WIDTH / 2.0,
			HEIGHT - (.6 * inch),
			contact['address'])
        canvas.drawRightString(
			WIDTH - (.4 * inch),
			HEIGHT - (.6 * inch),
			contact['email'])
        # restore the state to what it was when saved
        canvas.restoreState()
    return myPage

if __name__ == "__main__":
    contact = {
        'name': 'Nicholas Depinet',
        'website': 'http://github.com/nickdepinet/',
        'email': 'depinetnick@gmail.com',
        'address': '3092 Nathaniel Rochester Hall, Rochester, NY 14623',
        'phone': '(614)365-1089'}
    data = {
        'objective': ' '.join(['Seeking co-operative employment',
                    'in the field of software development or devops,',
                    'preferably working in python and/or web infrastructure, ',
                    'to start June 2014.']),
        'summary': ' '.join(['I love to use programming to solve interesting problems.',
                    'I am also a huge proponent of python - I love to learn more about the language',
                    'and exploit its quirks when I\'m solving problems&mdash;which is likely why I chose to',
                    'create my resume in python rather than something more conventional like latex.',
                    'My work and personal projects reflect my passion for python and my passion for solving problems.']),
        'education': '<br/>'.join(['<b>Rochester Insitute of Technology</b>',
                    '<b>B.S.</b>  Computer Science',
                    '<b>Expected Graduation</b>  2016']),
        'skills': '<br/>'.join(['<b>Languages</b>  Python, C, Java, PHP, Bash, jQuery, Haml/HTML, LESS/CSS',
                    '<b>Tools</b>  Git/Mercurial, Vim, Django, Tornado, Twisted, Autobahn, ReportLab',
                    '<b>Platforms</b>  Debian, RHEL, OSX, Windows, Cisco IOS',
                    '<b>Services</b>  MySQL, PostgreSQL, MongoDB, Apache/Nginx, HAProxy, Gunicorn',
                    '<b>Certifications</b>  Cisco Certified Network Associate (CCNA)']),
        'experience': [''.join(['<b>SpkrBar</b> - Columbus, OH<br/>',
                    '<alignment=TA_RIGHT>Software Developer: September 2013 - December 2013</alignment><br/>',
                    'Develop and maintain the front and backend of a startup website using Python and the Django framework. ',
                    'The website allows technical conferences, speakers, and attendees to connect and keep up to date. ',
                    'Primary Responsibilities include fixing bugs found in the website, implementing new features, and testing. ',
                    'Languages used include Python, Django, HTML, JavaScript, and CSS.<br/>']),
                    ''.join(['<b>STI-Healthcare</b> - Columbus, OH<br/>',
                    '<alignment=TA_RIGHT>Software Engineering Intern: May - August 2013</alignment><br/>',
                    'Developed a web application using Python and the Django framework ',
                    'to allow hospitals to easily store, search, and retrieve archived medical records. ',
                    'Primary Responsibility was the design and implementation of the metadata storage backend, ',
                    'as well as the search functionality (backend and frontend).<br/>']),
                    ''.join(['<b>Computer Science House</b> - Rochester, NY<br/>',
                    'Drink Administrator: February 2013 - Present<br/>',
                    'Responsible for managing the networked drink and snack machines at Computer Science House. ',
                    'Duties include maintaining the hardware of the machines, including fixing things when they broke, ',
                    'operating and maintaining the Node.JS Server, and maintaining the software used to run the system.<br/>']),
                    ''.join(['<b>STI-Healthcare</b> - Columbus, OH<br/>',
                    'Network & Server Administration Intern: May - August 2012<br/>',
                    'Maintained a small business network consisting of windows and linux machines and servers. ',
                    'Responsibilities included setting up VPN connections between the company and client hospitals, ',
                    ' and configuring and maintaining linux virtual servers to be used for testing and development.']),
                    ''.join(['<b>New Albany High School</b> - New Albany, OH<br/>',
                    'Life Guard and Water Safety Instructor: June 2009 - May 2012<br/>',
                    'Taught children ages 8-12 to swim, emphasizing safe water skills and overcoming their fears of the water. ',
                    'As the only lifeguard on duty, I was responsible for ensuring the safety of all patrons of the pool<br/>'])],
        'projects': [''.join(['<b>DrinkPi</b> - http://github.com/jeid64/drinkpi/<br/>',
                    'Worked with a partner to replace a failing component in the Computer Science House drink machines. ',
                    'The software controlling the machines was previously written in java and running on Dallas TINI microcomputers. ',
                    'These TINI\'s were failing and were no longer produced, so we re-wrote the software in python to run on a ',
                    'Raspberry Pi. The software talks to the drink server over sockets using the SUNDAY protocol, and to the drink ',
                    'machine hardware using the 1-Wire protocol and a usb 1-Wire bus master.']),
                    ''.join(['<b>TempMon</b> - http://github.com/nickdepinet/tempmon/<br/>',
                    'Implemented a temperature monitoring system for a server room using a Raspberry Pi. ',
                    'The system monitors temperature using a series of DSB1820 temperature sensors. ',
                    'When the temperature exceeds a set limit, an email notification is sent. ',
                    'The software, including temperature reading, threading, and email notification is written in python.']),
                    ''.join(['<b>IBM Master the Mainframe Competition</b><br/>',
                    'I have been a part 2 completionist in IBM\'s yearly Master the Mainframe competetion every year I have competed ',
                    'since 2008. In addition, in 2011 I was one of the first 100 competitors to finish part 2 of the competition, ',
                    'and therefore was a part 2 winner for 2011. This contest has given me experience working with mainframes and the Job Control Language (JCL).'])],}
    tblData = [
        ['OBJECTIVE', Paragraph(data['objective'], styles['Content'])],
        ['SUMMARY', Paragraph(data['summary'], styles['Content'])],
        ['EDUCATION', Paragraph(data['education'], styles['Content'])],
        ['SKILLS', Paragraph(data['skills'], styles['Content'])],
        ['EXPERIENCE', [Paragraph(x, styles['Content']) for x in data['experience']]],
        ['PROJECTS', [Paragraph(x, styles['Content']) for x in data['projects']]]
        ]
    generate_print_pdf(tblData, contact)
