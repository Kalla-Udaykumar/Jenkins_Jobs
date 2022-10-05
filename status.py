from jenkinsapi.jenkins import Jenkins
from jenkinsapi.custom_exceptions import NoBuildData
from requests import ConnectionError

def get_job_by_build_state(url, view_name, state='FAILURE'):
    server = Jenkins(url)
    view_url = f'{url}/view/{view_name}/'
    view = server.get_view_by_url(view_url)
    jobs = view.get_job_dict()

    jobs_by_state = []

    for job in jobs:
        job_url = f'{url}/{job}'
        j = server.get_job(job)
        try:
            build = j.get_last_completed_build()
            status = build.get_status()
            if status == state:
                jobs_by_state.append(job)
                except ConnectionError
                    continue
    return jobs_by_state

if __name__ == '__main__':
    jobs = get_job_by_build_state(url='https://cbjenkins-pg.devtools.intel.com/teams-iotgdevops01/job/iotgdevops01', view_name='All', state='FAILURE')
