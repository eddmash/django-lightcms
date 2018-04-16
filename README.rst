A Cms for Developers
====================

This a very basic cms to incorporate in your django project.

Its not meant to be a full scale cms, if you need a website your better of using a fullblown cms.

The idea behind this simple is.
- create project for client.
- client says 'put this content on the app e.g terms and condition, about app but
i don't need a website'.
- client gives word document with the content.
- your paste it onto a static html page and your done.
- few months down the line, client say, add this content, change that content. this is what this
tries to avoid.
- it lets the client add, update, delete static content without you being needed.


```html

    <table class="table table-condensed table-hover table-bordered">
        <thead>
        <tr>
            <th>Title</th>
            <th>Published</th>
            <th>Parent</th>
            <th>Menu Order</th>
            <th>author</th>
            <th>created on</th>
            <th colspan="3" class="text-center">Actions</th>
        </tr>
        </thead>
        <tbody>


        {% for page in page_list %}
            <tr>
                <td>
                    <a href="{% url "cms:page-edit" page.slug %}">
                        <small>{{ parent }} ></small>
                        {{ page.title }}
                    </a>
                </td>
                <td>
                    {{ page.get_publish_display }}
                </td>
                <td>
                    {{ page.parent }}
                </td>
                <td>
                    {{ page.order }}
                </td>
                <td>
                    {{ page.author }}
                </td>
                <td>
                    {{ page.created_on }}
                </td>
                <td>
                    <i class="fa fa-pencil-square-o"></i>
                    <a href="{% url "cms:page-edit" page.slug %}">
                        {% trans "Edit" %}
                    </a>
                </td>
                <td>
                    <i class="fa fa-times-circle-o"></i>
                    <a href="{% url "cms:page-delete" page.slug %}">{% trans "Delete" %}</a>
                </td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
```