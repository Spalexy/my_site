from django.core.management.base import BaseCommand
from main_app.models import Job_place, St_place, Organisation


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        organisations = [
            {'name': 'РГУПС', 'region': 'Ростов-на-Дону', 'site': 'http://www.rgups.ru', 'phone': '+71234567889'},
            {'name': 'ООО Аргуссофт', 'region': 'Москва', 'site': 'http://argussoft.ru/', 'phone': '+71234567889'},
            {'name': 'ГК Прибор-Системы', 'region': 'Москва', 'site': 'http://pribor-systems.ru/',
             'phone': '+71234567889'},
            {'name': 'ООО СПД', 'region': 'Москва', 'site': 'http://www.spd-msk.ru/', 'phone': '+71234567889'},
        ]

        job_places = [
            {'j_name': 'РГУПС', 'position': 'Инженер НИЛ',
              'resp': 'Разработка системы диспетчерского контроля и управления', 'period': 2},
            {'j_name': 'ГК Прибор-Системы', 'position': 'Инженер по внедрению',
              'resp': 'Внедрение электронных компонентов в проекты заказчика', 'period': 1.5},
            {'j_name': 'ООО Аргуссофт', 'position': 'Инженер по внедрению',
              'resp': 'Внедрение электронных компонентов в проекты заказчика', 'period': 2},
            {'j_name': 'ООО СПД', 'position': 'Инженер',
             'resp': 'Пуско-наладка серверного и сетевого оборудования, ЛВС, СВН', 'period': 1}
        ]

        st_places = [
            {
                'st_place': 'Ростовский государственный университет путей сообщения',
                'st_time': '2005-2010',
                'department': 'Автоматика, телемеханика и связь на ж.-д. транспорте',
                'specialisation': 'Автоматика и телемеханика на ж.-д. транспорте',
            },
        ]

        Organisation.objects.all().delete()
        for organisation in organisations:
            organisation = Organisation.objects.create(**organisation)

        Job_place.objects.all().delete()
        for job in job_places:
            org_name = job["j_name"]
            organisation = Organisation.objects.get(name=org_name)
            job['j_name'] = organisation
            job = Job_place.objects.create(**job)

        # Work.objects.all().delete()
        # for work in works:
        #     org_name = work["organization"]
        #     # Получаем организацию по имени
        #     organization = Organization.objects.get(name=org_name)
        #     # Заменяем название организации объектом
        #     work['organization'] = organization
        #     work = Work(**work)
        #     work.save()

        St_place.objects.all().delete()
        for study in st_places:
            study = St_place.objects.create(**study)
            
