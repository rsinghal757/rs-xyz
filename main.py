import os
from fasthtml.common import *

# Initialize the FastHTML app
app, rt = fast_app(live=True)

### FUNCTIONS ###


# Define the base HTML template using TailwindCSS
def base_template(page_title, content):
    description = "Selected software, hardware, and research projects by Rohit Singhal."
    return Html(
        Head(
            Title(page_title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Meta(name="description", content=description),
            Meta(property="og:title", content=page_title),
            Meta(property="og:description", content=description),
            Meta(property="og:type", content="website"),
            Meta(name="twitter:card", content="summary"),
            Link(
                rel="icon",
                href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>",
            ),
            Link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            ),
        ),
        Body(
            Div(
                content,
                cls="bg-white text-gray-900 min-h-screen p-4 sm:p-4 md:p-8 lg:p-16 xl:p-36 xl:pt-16 xl:pb-12 font-serif flex flex-col items-stretch",
            )
        ),
    )


# Function to get projects
def get_projects():
    return [
        {
            "title": "GizzNote",
            "description": "A lightweight document editor for reading, writing, note-taking, and journaling. Keep ideas in Markdown, connect them with wikilinks, and talk to your notes when useful.",
            "links": [
                {"label": "Open GizzNote ↗", "url": "https://gizznote.com"},
                {
                    "label": "View source →",
                    "url": "https://github.com/rsinghal757/agentmem",
                },
            ],
            "image": "assets/gizznote.svg",
        },
        {
            "title": "Pebble",
            "description": "An AI tutor for K-12 students that helps them learn programming by building their own projects.",
            "links": [{"label": "Open Pebble ↗", "url": "https://getpebble.in"}],
            "image": "assets/pebble-1.png",
        },
        {
            "title": "Reader-1",
            "description": "A cyberdeck e-reader built with a Raspberry Pi and a Waveshare E-Ink display.",
            "links": [],
            "image": "assets/reader-1.png",
        },
        {
            "title": "BabyARC",
            "description": "A tiny abstraction and reasoning dataset inspired by François Chollet's Abstraction and Reasoning Corpus.",
            "links": [
                {
                    "label": "View source →",
                    "url": "https://github.com/rsinghal757/babyARC",
                }
            ],
            "image": "assets/babyarc.svg",
        },
        {
            "title": "AiTone",
            "description": "A browser-based music coding environment built with Tone.js, with an AI collaborator for modifying the music through natural language.",
            "links": [
                {"label": "Open AiTone ↗", "url": "https://ai-tone.netlify.app/"}
            ],
            "image": "assets/aitone-1.png",
        },
        {
            "title": "Email Signature Generator",
            "description": "A mobile-first tool for creating, customizing, previewing, and copying HTML email signatures.",
            "links": [
                {
                    "label": "Create a signature ↗",
                    "url": "https://emailsignature.in",
                }
            ],
            "image": "assets/emailsig-1.png",
        },
    ]


# Function to get social links
def get_social_links():
    return [
        {"platform": "Twitter", "url": "https://x.com/0xRohitSinghal"},
        {"platform": "GitHub", "url": "https://github.com/rsinghal757"},
        {
            "platform": "LinkedIn",
            "url": "https://www.linkedin.com/in/rsinghal757/",
        },
        {"platform": "Medium", "url": "https://medium.com/@rsinghal757"},
        {
            "platform": "Portfolio",
            "url": "https://www.figma.com/proto/P8VfPiBlPuPYWsPqL5z2TM/Work_Compilation?node-id=32-21535&t=aVwbWlahk1NcbnBf-0&scaling=min-zoom&content-scaling=fixed&page-id=31%3A18497&hide-ui=1",
        },
    ]


def project_card(project):
    project_links = [
        A(
            link["label"],
            href=link["url"],
            target="_blank",
            rel="noopener noreferrer",
            cls="text-gray-700 hover:underline text-base md:text-lg",
        )
        for link in project.get("links", [])
    ]

    return Div(
        Div(
            Div(
                H3(
                    project["title"],
                    cls="text-xl md:text-2xl font-medium font-serif",
                ),
                P(
                    project["description"],
                    cls="text-gray-600 text-base md:text-lg mt-2",
                ),
                cls="flex flex-col items-start",
            ),
            Div(*project_links, cls="flex flex-wrap gap-4 mt-6 md:mt-10")
            if project_links
            else None,
            cls="flex flex-col items-stretch justify-between w-full md:max-w-md",
        ),
        Img(
            src=project["image"],
            alt=f"{project['title']} project visual",
            cls="w-full md:w-2/3 mt-2 md:mt-0",
        ),
        cls="border-b pb-8 md:pb-16 pt-8 md:pt-16 flex flex-col md:flex-row "
        "items-start justify-between gap-6 md:gap-10",
    )


# Homepage route
@rt("/")
def get():
    projects = get_projects()
    social_links = get_social_links()
    body_content = Div(
        Div(
            Div(
                H3(
                    "Rohit Singhal",
                    cls="text-3xl md:text-4xl lg:text-5xl font-bold font-serif leading-tight",
                ),
                Div(
                    *[
                        A(
                            link["platform"],
                            href=link["url"],
                            target="_blank",
                            rel="noopener noreferrer",
                            cls="text-gray-600 font-serif hover:underline text-sm md:text-base",
                        )
                        for link in social_links
                    ],
                    cls="flex flex-row flex-wrap text-gray-500 gap-x-4 gap-y-2 lg:gap-x-8",
                ),
                cls="flex flex-col items-start space-y-2 mb-4",
            ),
            Div(
                H3(
                    "The world is a museum of passion projects.",
                    cls="text-gray-900 font-serif text-base md:text-lg italic",
                ),
                Div(
                    A(
                        "John Collison",
                        href="https://x.com/collision/status/1529452415346302976",
                        target="_blank",
                        rel="noopener noreferrer",
                        cls="text-gray-500 italic text-right text-sm md:text-base",
                    ),
                    P(", Stripe", cls="text-gray-500 italic text-right text-sm md:text-base"),
                    cls="flex flex-row items-end",
                ),
                cls="flex flex-col items-start md:items-end space-y-0 mt-4",
            ),
            cls="flex flex-col md:flex-row justify-between items-start mb-8 md:mb-12",
        ),
        Div(
            P(
                "I'm Rohit. For money and fun, I do software design and engineering.",
                cls="text-gray-600 text-base md:text-lg",
            ),
            cls="flex flex-col items-start space-y-2 mb-8 md:mb-12 max-w-2xl",
        ),
        Div(
            H2(
                "Selected Projects",
                cls="text-2xl md:text-3xl font-medium font-serif border-b pb-4 md:pb-8 text-left",
            ),
            *[project_card(project) for project in projects],
            cls="p-0 mb-12 md:mb-24",
        ),
        cls="max-w-7xl w-full leading-relaxed space-y-12",
    )
    return base_template("Rohit Singhal", body_content)


serve(port=int(os.environ.get("PORT", 5001)))
