from fasthtml.common import *

# Initialize the FastHTML app
app, rt = fast_app(live=True)

### FUNCTIONS ###

# Define the base HTML template using TailwindCSS
def base_template(page_title, content):
    return Html(
        Head(
            Title(page_title),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/uikit@3.16.26/dist/css/uikit.min.css"),
            Script(src="https://cdn.jsdelivr.net/npm/uikit@3.16.26/dist/js/uikit.min.js"),
            Script(src="https://cdn.jsdelivr.net/npm/uikit@3.16.26/dist/js/uikit-icons.min.js"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        ),
        Body(
            Div(
                content,
                cls="bg-[#fff] text-gray-900 min-h-screen p-4 sm:p-4 md:p-8 lg:p-16 xl:p-36 xl:pt-16 xl:pb-12 font-serif flex flex-col items-stretch"
            )
        ),
    )

# Function to get projects
def get_projects():
    return [
        {
            "title": "Pebble",
            "description": "An AI-tutor for K-12 students to help them learn programming and build their own projects.",
            "link": "https://getpebble.in",
            "image": "assets/pebble-1.png",
        },
        {
            "title": "Reader-1",
            "description": "A cyberdeck e-reader built with a Raspberry Pi and a Waveshare E-Ink display.",
            "link": None,
            "image": "assets/reader-1.png",
        },
        {
            "title": "BabyARC",
            "description": "BabyARC is a tiny abstraction and reasoning dataset inspired by the original Abstraction and Reasoning Corpus by Francois Chollet.",
            "link": "https://github.com/rsinghal757/babyARC",
            "image": None,
        },
        {
            "title": "AiTone",
            "description": "AiTone is a web application that allows users to write and execute music code in the browser using Tone.js, with the ability to modify the code using natural language requests processed by AI.",
            "link": "https://ai-tone.netlify.app/",
            "image": "assets/aitone-1.png",
        },
        {
            "title": "Email Signature Generator",
            "description": "An email signature generator that allows users to create and customize email signatures with their name, title, and contact information.",
            "link": "https://emailsignature.in",
            "image": "assets/emailsig-1.png",
        },
    ]

# Function to get social links
def get_social_links():
    return [
        {"platform": "Twitter", "url": "https://x.com/0xRohitSinghal"},
        {"platform": "GitHub", "url": "https://github.com/rsinghal757"},
        {"platform": "LinkedIn", "url": "https://www.linkedin.com/in/rsinghal757/"},
        {"platform": "Medium", "url": "https://medium.com/@rsinghal757"},
    ]

# Homepage route
@rt("/")
def get():
    projects = get_projects()
    social_links = get_social_links()
    body_content = Div(
        Div(
            Div(
                H3("Rohit Singhal", cls="text-3xl md:text-4xl lg:text-5xl font-bold font-serif leading-tight"),
                Div(
                    *[A(link["platform"], href=link["url"], target="_blank", cls="text-gray-600 font-serif hover:underline text-sm md:text-base") for link in social_links],
                    cls="flex flex-row text-gray-500 space-x-4 lg:space-x-8"
                ),
                cls="flex flex-col items-left space-y-2 mb-4"
            ),
            Div(
                H3("The world is a museum of passion projects.", cls="text-gray-900 font-serif text-base md:text-lg italic"),
                Div(
                    A("John Collison", href="https://x.com/collision/status/1529452415346302976", cls="text-gray-500 italic text-right text-sm md:text-base"),
                    P(", Stripe", cls="text-gray-500 italic text-right text-sm md:text-base"),
                    cls="flex flex-row items-end"
                ),
                cls="flex flex-col items-start md:items-end lg:items-end xl:items-end space-y-0 mt-4"
            ),
            cls="flex flex-col md:flex-row justify-between items-start mb-8 md:mb-12"
        ),
        Div(
            P("I'm Rohit. For money and fun, I do software design and engineering.", cls="text-gray-600 text-base md:text-lg"),
            cls="flex flex-col items-left space-y-2 mb-8 md:mb-12 max-w-2xl"
        ),
        Div(
            H2("Work", cls="text-2xl md:text-3xl font-medium font-serif border-b pb-4 md:pb-8 text-left"),
            *[Div(
                Div(
                    Div(
                        H3(project["title"], cls="text-xl md:text-2xl font-medium font-serif"),
                        P(project["description"], cls="text-gray-500 text-base md:text-lg"),
                        cls="flex flex-col items-left space-y-2"
                    ),
                    A("View Project →", href=project["link"], target="_blank", cls="text-gray-600 mt-6 md:mt-12 hover:underline text-base md:text-lg") if project["link"] else None,
                    cls="flex flex-col items-stretch justify-between w-full"
                ),
                Img(src=project["image"], alt=project["title"], cls="w-full md:w-2/3 mt-4 md:mt-0") if project["image"] else None,
                cls="border-b pb-8 md:pb-16 pt-8 md:pt-16 flex flex-col md:flex-row items-center md:items-start lg:items-start xl:items-start justify-between space-x-0 md:space-x-4 lg:space-x-4 xl:space-x-4"
            ) for project in projects],
            cls="p-0 mb-12 md:mb-24"
        ),
        cls="max-w-7xl w-full leading-relaxed space-y-12"
    )
    return base_template("Rohit Singhal", body_content)

# Run the app on port 5001
serve(port=5001)
