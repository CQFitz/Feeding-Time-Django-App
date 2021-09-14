from django.db import models
from tinyhtml import html, h, Frag, frag


# layout for html https://pypi.org/project/tinyhtml/
def layout(title: str, body: Frag) -> Frag:
    return html()(
        h("head")(
            h("title")(title),
            h("link", href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC", crossorigin="anonymous"),
        ),
        h("body", klass="container")(body)
    ).render()


class Staff(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    staff_details = models.CharField(max_length=100, blank=True, default='') # This is set to be name of staff
    html_content = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        # get data from staff_details onto a variable
        # those variable set in to a set create of data and save to html_content variable
        create_html = layout(self.staff_details, frag(
            h("h1")("Staff Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.staff_details),
        ))

        self.html_content = create_html
        super(Staff, self).save(*args, **kwargs)

    def __str__(self):
        return self.staff_details


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    event_name = models.CharField(max_length=100, blank=True, default='')
    event_description = models.CharField(max_length=100)
    other_details = models.CharField(max_length=100)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    html_content = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        create_html = layout(self.event_name, frag(
            h("h1")("Event Name"),
            h("h2")(self.event_name),
            h("h1")("Event Description"),
            h("h2")(self.event_description),
            h("h1")("Event Detail"),
            h("p")(self.other_details),
        ))

        self.html_content = create_html
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.event_name


class Food(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    food_details = models.CharField(max_length=50, blank=True, default='')
    html_content = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        create_html = layout(self.food_details, frag(
            h("h1")("Food Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.food_details),
        ))

        self.html_content = create_html
        super(Food, self).save(*args, **kwargs)

    def __str__(self):
        return self.food_details


class Animal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    animal_details = models.CharField(max_length=60, blank=True, default='')
    html_content = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        create_html = layout(self.animal_details, frag(
            h("h1")("Animal Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.animal_details),
        ))

        self.html_content = create_html
        super(Animal, self).save(*args, **kwargs)

    def __str__(self):
        return self.animal


class FoodInAnEvent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    food_id = models.ForeignKey('Food', on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    html_content = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        create_html = layout(self.food_id, frag(
            h("h1")("Food Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.food_id),
            h("br"),
            h("h1")("Event Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.event_id),
            h("br"),
            h("h1")("Staff Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.event_id.staff_id)
        ))

        self.html_content = create_html
        super(FoodInAnEvent, self).save(*args, **kwargs)


class AnimalInAnEvent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    html_content = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        create_html = layout(self.animal_id, frag(
            h("h1")("Animal Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.animal_id),
            h("br"),
            h("h1")("Event Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.event_id),
            h("br"),
            h("h1")("Staff Detail"),
            h("hr"),
            h("h1")("Name"),
            h("h2")(self.event_id.staff_id)
        ))

        self.html_content = create_html
        super(AnimalInAnEvent, self).save(*args, **kwargs)