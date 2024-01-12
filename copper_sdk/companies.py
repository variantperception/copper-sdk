from copper_sdk.base import BaseResource


class Companies(BaseResource):
    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/companies/{id}")

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post("/companies", body)

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f"/companies/{id}", body)

    def delete(self, id):
        return self.copper.delete(f"/companies/{id}")

    def list(self, body=None):
        if body is None:
            body = {}
        default_body = {
            "page_number": 1,  # number	The page number (starting with 1) that you would like to view.	1
            "page_size": 20,  # number	The number of entries included in a page of results	20
            "sort_by": "date_modified",  # string	The field on which to sort the results (see footnote 1).
            "sort_direction": "asc",  # string	The direction in which to sort the results. Possible values are: asc or desc.
        }

        return self.copper.post("/companies/search", {**default_body, **body})

    def list_related(self, id):
        return self.copper.get(f"/companies/{id}/related")

    def relate_to(self, id, relative_type, related_id):
        body = {"resource": {"id": related_id, "type": relative_type}}

        return self.copper.post(f"/companies/{id}/related", json_body=body)

    def unrelate_from(self, id, relative_type, related_id):
        body = {"resource": {"id": related_id, "type": relative_type}}

        return self.copper.delete(f"/companies/{id}/related", json_body=body)

    def activities(self, id):
        return self.copper.get(f"/companies/{id}/activities")

    def contact_types(self):
        return self.copper.get("/contact_types")
