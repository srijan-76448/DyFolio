import json


class CV:
    def __init__(self, source, destination):
        with open(source, "r") as f:
            self.data = dict(json.load(f))

        self.source = source
        self.destination = destination

    def _generate_personal_info(self):
        ret = '\n## Personal Information\n'
        for key, value in self.data['Personal Information'].items():
            if key == 'Connections':
                ret += f'- **{key}**:\n'
                for k, v in value.items():
                    ret += f'  - [{k}]({v})\n'
            elif key == 'Location':
                ret += f'- **{key}**: [{value["Address"]}]({value["Link"]})\n'
            elif key == 'Education':
                ret += f'- **{key}**:\n'
                for k, v in value.items():
                    ret += f'  - {k}: {v}\n'
            else:
                ret += f'- **{key}**: {value}\n'

        return ret

    def _generate_education(self):
        ret = '\n## Education\n'
        for ed in self.data['Education']:
            if ed['Completed']:
                ret += f'- **{ed["Degree"]}** in **{ed["Branch"]}** at [{ed["University"]}]({ed["University Link"]})\n'

            else:
                ret += f'- {ed["Stage"]} year **{ed["Degree"]}** Student in **{ed["Branch"]}** at [{ed["University"]}]({ed["University Link"]})\n'

        return ret

    def _generate_summary(self):
        ret = '\n## Summary\n'
        for line in self.data['Summary']:
            ret += f'{line}\n'

        return ret

    def _generate_experience(self):
        ret = '\n## Experience\n'
        for exp in self.data['Experience']:
            ret += f'- **{exp["Title"]}** ({exp["Timeline"]})\n'
            for line in exp['Achievements']:
                ret += f'  - {line}\n'

        return ret

    def _generate_skill_set(self):
        ret = '\n## Skill Set\n'
        for key, value in self.data['Skill Set'].items():
            ret += f'- **{key}**: ' + ', '.join(value) + '\n'

        return ret

    def _generate_projects(self):
        ret = '\n## Projects\n'
        for project, info in self.data['Projects'].items():
            ret += f'- **[{project}]({info["Link"]})** ({info["Timeline"]})\n'
            for line in info['Description']:
                ret += f'  - {line}\n'
            if 'Used Modules for this project' in info:
                ret += '  - Used Modules for this project:\n'
                for k, v in info['Used Modules for this project'].items():
                    ret += f'    - **{k}:** {v}\n'
            if 'Connections' in info:
                ret += '  - Connections:\n'
                for k, v in info['Connections'].items():
                    ret += f'    - [{k}]({v})\n'

        return ret

    def _generate_certifications(self):
        ret = '\n## Certifications\n'
        for line in self.data['Certifications']:
            ret += f'- {line}\n'

        return ret

    def _generate_documents(self):
        ret = '\n## Documents\n'
        for line in self.data['Documents']:
            ret += f'- [{line}]({self.data["Documents"][line]})\n'

        return ret

    def update_cv(self, content, filename):
        with open(filename, 'w') as f:
            f.write(content)

        print("\033[92m[+] \033[1mDynamicCVGenerator: \033[0m\033[92mCV Updated successfully!\033[0m")

    def main(self):
        ret = '# Curriculum Vitae (CV)\n'
        terminal_statement = '\n## Thanks'

        personal_info = self._generate_personal_info()
        education = self._generate_education()
        summary = self._generate_summary()
        experience = self._generate_experience()
        skill_set = self._generate_skill_set()
        projects = self._generate_projects()
        certifications = self._generate_certifications()
        documents = self._generate_documents()

        content = ret + personal_info + education + summary + experience + skill_set + projects + certifications + documents + terminal_statement + '\n'

        try:
            self.update_cv(content, self.destination)
            return None

        except Exception as e:
            print(f"\033[91m[-] \033[1mDynamicCVGeneratorError: \033[0m\033[91m{e}\033[0m")
            return content
