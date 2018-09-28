import json


class Json_fixtures:

    @staticmethod
    def create_ticket_json(value):
        baseJson = {"fields": {
            "project":
                {
                    "key": "AQAPYTHON"
                },
            "summary": value,
            "description": "Creating of an issue using the REST API",
            "issuetype": {
                "name": "Bug"
            }}}
        return json.dumps(baseJson)

    @staticmethod
    def update_priority_json(new_priority):
        baseJson = {"fields": {
            "priority": {
                "name": new_priority
            }}}
        return json.dumps(baseJson)

    @staticmethod
    def update_ticket_json(field, new_value):
        baseJson = {"fields": {field: new_value}}
        return json.dumps(baseJson)

