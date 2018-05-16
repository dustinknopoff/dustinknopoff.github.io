import json


class Section:
    def __init__(self, title, link):
        """
        Initializes a section.
        :param title: The title of this section.
        :param link: It's associated link.
        """
        self.title = title
        self.link = link
        self.items = []

    def add_item(self, content):
        """
        Adds a dictionary to self.items
        :param content: Dictionary of elements in a section.
        """
        self.items.append(content)
        print("Job added!")

    def __iter__(self):
        """
        Override iteration to loop through self.items.
        """
        for value in self.items:
            yield value

    def export_content(self):
        """
        Converts parameters of this section to a dictionary.
        :return: dictionary of parameters in this section.
        """
        d = {'title': self.title, 'link': self.link, 'info': list(self)}
        return d

    def export_html(self):
        """
        Fills parameters into HTML template
        :return: formatted string to match HTML template.
        """
        results = f"""
        <div class="{self.title}" id="#{self.link}">
        """
        for item in self.items:
            if type(self.items[0]) is not dict:
                results += f"""
                <h1>{item}</h1>
                """
            else:
                results += f"""
                <div class="my-card">
                    <div class="space">
                        <h1>{item['title'] if 'title' in item.keys() else item['degree']}</h1>
                        <h3>{item['company'] if 'company' in item.keys() else item['school']}</h3>
                        <p>{item['date']} <br /> {item['location'] if 'location' in item.keys() else ""} <br /> 
                        {item['description'] if 'description' in item.keys() else ""}</p>
                        </div>
                    </div>
                </div>
                """
        results += "</div>"
        return results

class Defaults:



with open('/Users/Dustin/Documents/Gits/Web/dustinknopoff.github.io/src/templates/data.json', 'r') as f:
    data = json.load(f)
    sections = data['sections']
    for section in sections:
        sec = Section(section['name'], section['link'])
        for item in section['info']:
            sec.add_item(item)
        print(sec.export_html())
