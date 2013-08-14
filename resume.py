from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus.flowables import Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfdoc
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont

# Import our font
registerFont(TTFont('Inconsolata', 'fonts/Inconsolata-Regular.ttf'))
registerFont(TTFont('InconsolataBold', 'fonts/Inconsolata-Bold.ttf'))

# Set the page height and width
HEIGHT = 11 * inch
WIDTH = 8.5 * inch
styles = getSampleStyleSheet()


def generate_print_pdf(data, contact):
    pdfname = 'resume.pdf'
    doc = SimpleDocTemplate(
        pdfname,
        pagesize=letter,
        bottomMargin=.5 * inch,
        topMargin=.7 * inch,
        rightMargin=.5 * inch,
        leftMargin=.5 * inch)  # set the doc template
    style = styles["Normal"]  # set the style to normal
    story = []  # create a blank story to tell
    story.append(Paragraph(data, style))
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
        #reset the font
        canvas.setFont('Inconsolata', 10)
        # restore the state to what it was when saved
        canvas.restoreState()
    return myPage

if __name__ == "__main__":
	contact = {
				'name': 'Nick Depinet',
				'website': 'http://github.com/nickdepinet/',
				'email': 'depinetnick@gmail.com',
				'address': '3092 Nathaniel Rochester Hall, Rochester, NY 14623',
				'phone': '(614)365-1089'}
	data = "Here is where the actual resume stuff will go"
	generate_print_pdf(data, contact)
