from flask import Flask, render_template, url_for
app = Flask(__name__)

projects = [
    {
        'title' : 'Chess engine',
        'p_img' : 'photo/chess.png',
        'description': 'A simple chess engine, written in Processing, which provides players with an interactive playground and tools to plan out their strategies',
        'color' : 1,
        'demo': True,
        'GH_link': 'https://github.com/nathan20021/Chess',
        'YT_link': 'https://www.youtube.com/watch?v=PGa61f5q4bk&feature=youtu.be'
    },
    {
        'title' : 'L.E.D Cube',
        'p_img' : 'photo/cube.png',
        'description': 'A programable 3x3x3 Led Cube which has multiple pre-set lighting configurations. You can also play 3d snake on this low resolution display!',
        'color' : 2,
        'demo': False,
        'GH_link': 'https://github.com/nathan20021/Complete-LED-Cube-project'
    },
    {
        'title' : 'A* Visualization',
        'p_img' : 'photo/A star.png',
        'description': 'Visualize the famous A* path finding algorithm with an interactive playground. Users can draw walls, choose their destinations and the shortest path will reveal',
        'color' : 3, 
        'demo': True,
        'GH_link': 'https://github.com/nathan20021/A_star_visualization',
        'YT_link': 'https://youtu.be/82DPwMUWq1Q'
    },
    {
        'title' : 'Portfolio',
        'p_img' : 'photo/Computer.png',
        'description': 'Made possible with the help of Adobe XD, Adobe Illustrator, Python Flask, HTML5, CSS3 and JavaScript.',
        'color' : 4,
        'demo': False,
        'GH_link': 'https://github.com/nathan20021/Portfolio'
    },
]

skills =[
    {
        'category': 'Software Development',
        'sub_skills': [
            ['Python', ['OOP, ', 'Kivy, ','Panda, ','Numpy, ', 'OpenCV, ', 'Pygame'], 4],
            ['C++/ Arduino', ['Native Arduino, ', 'Sensors, ','Port Manipulation'], 3],
            ['Java/ Processing', ['OOP, ', 'GUI, ','Data Visualization, ','2D Games'], 3]
        ]
    },
    {
        'category': 'Web Developemnt',
        'sub_skills': [
            ['HTML5/ CSS3/ JavaScript', ['Native, ','Bootstrap, ','Media Queries, ', 'SCSS, ', 'API, ','Common JS Libraries'], 2],
            ['Web Design', ['Adobe XD, ', 'Webflow'], 2.5],
            ['Back-end', ['Python Flask, ', 'Django, ','Node.JS',], 1.5],
            ['Database: SQL', [], 1],
            ['Hosting', ['Google Firebase, ', 'Heroku'], 1]
        ]
    }, 
    {
        'category': 'Related Skills',
        'sub_skills': [
            ['Microsoft Office Suite', [], 4],
            ['PCB Design', ['PCB Wizard, ', 'Altinum'], 2.5],
            ['Adobe Software', ['Illustrator, ', 'Photoshop, ','Premiere Pro',], 2.5],
            ['Autodesk Inventor', [], 0.5]
        ]
    }
]

_1p13_projects =[
    {
        'title' : 'Project One : Renewable technology challenge',
        'descriptions': 'Mechanical design of turbine blades in renewable wind technology',
        'Final_Deliverable_link': 'PDF/P1/final.pdf',
        'Log_Book_link': 'PDF/P1/log.pdf',
        'Milestone_link': 'PDF/P1/Milestones.pdf'
    },

    {
        'title' : 'Project Two : Get a Grip',
        'descriptions': 'Design a System for Sterilizing Surgical Tools using Remote Sensing and Actuation',
        'Final_Deliverable_link': 'PDF/P2/final.pdf',
        'Log_Book_link': 'PDF/P2/log.pdf',
        'Milestone_link': 'PDF/P2/Milestones.pdf'
    }
]

color_classes = ['color_1', 'color_2', 'color_3', 'color_4']

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', projects=projects, color_classes = color_classes)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/1p13')
def _1p13():
    return render_template('1p13.html', data=_1p13_projects)

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port = 8080)