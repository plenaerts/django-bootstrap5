from django import forms

from .base import BootstrapTestCase


class SelectTestForm(forms.Form):
    test = forms.ChoiceField(
        choices=(
            (1, "one"),
            (2, "two"),
        ),
        widget=forms.RadioSelect,
    )


class DisabledSelectTestForm(forms.Form):
    test = forms.ChoiceField(
        choices=(
            (1, "one"),
            (2, "two"),
        ),
        widget=forms.RadioSelect,
        disabled=True,
    )


class RadioSelectWithDisabledOptions(forms.RadioSelect):
    def __init__(self, attrs=None, choices=(), *, disabled_values=()):
        super().__init__(attrs)
        self.choices = choices
        self.disabled_values = set(disabled_values)

    def create_option(self, name, value, *args, **kwargs):
        option = super().create_option(name, value, *args, **kwargs)
        if value in self.disabled_values:
            option["attrs"]["disabled"] = True
        return option


class DisabledOptionSelectTestForm(forms.Form):
    test = forms.ChoiceField(
        choices=(
            (1, "one"),
            (2, "two"),
        ),
        widget=RadioSelectWithDisabledOptions(disabled_values={1}),
    )


class BootstrapFieldSelectTestCase(BootstrapTestCase):
    def test_select(self):
        """Test field with select widget."""
        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test %}", context={"form": SelectTestForm()}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label class="form-label">Test</label>'
                '<div class="" required id="id_test">'
                '<div class="form-check">'
                '<input class="form-check-input" type="radio" name="test" id="id_test_0" value="1">'
                '<label class="form-check-label" for="id_test_0">one</label>'
                "</div>"
                '<div class="form-check">'
                '<input class="form-check-input" type="radio" name="test" id="id_test_1" value="2">'
                '<label class="form-check-label" for="id_test_1">two</label>'
                "</div>"
                "</div>"
                "</div>"
            ),
        )

    def test_select_horizontal(self):
        """Test field with select widget in horizontal layout."""
        self.assertHTMLEqual(
            self.render('{% bootstrap_field form.test layout="horizontal" %}', context={"form": SelectTestForm()}),
            (
                '<div class="django_bootstrap5-req row mb-3">'
                '<label class="col-sm-2 col-form-label">Test</label>'
                '<div class="col-sm-10">'
                '<div class="" required id="id_test">'
                '<div class="form-check">'
                '<input class="form-check-input" type="radio" name="test" id="id_test_0" value="1">'
                '<label class="form-check-label" for="id_test_0">one</label>'
                "</div>"
                '<div class="form-check">'
                '<input class="form-check-input" type="radio" name="test" id="id_test_1" value="2">'
                '<label class="form-check-label" for="id_test_1">two</label>'
                "</div>"
                "</div>"
                "</div>"
                "</div>"
            ),
        )

    def test_select_floating(self):
        """Test field with select widget in floating layout."""
        self.assertHTMLEqual(
            self.render('{% bootstrap_field form.test layout="floating" %}', context={"form": SelectTestForm()}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label class="form-label">Test</label>'
                '<div class="" required id="id_test">'
                '<div class="form-check">'
                '<input class="form-check-input" type="radio" name="test" id="id_test_0" value="1">'
                '<label class="form-check-label" for="id_test_0">one</label>'
                "</div>"
                '<div class="form-check">'
                '<input class="form-check-input" type="radio" name="test" id="id_test_1" value="2">'
                '<label class="form-check-label" for="id_test_1">two</label>'
                "</div>"
                "</div>"
                "</div>"
            ),
        )

    def test_disabled_select(self):
        """Test field with disabled select widget."""
        self.maxDiff = None
        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test %}", context={"form": DisabledSelectTestForm()}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label class="form-label">Test</label>'
                '<div class="" disabled required id="id_test">'
                '<div class="form-check">'
                '<input class="form-check-input" disabled type="radio" name="test" id="id_test_0" value="1">'
                '<label class="form-check-label" for="id_test_0">one</label>'
                "</div>"
                '<div class="form-check">'
                '<input class="form-check-input" disabled type="radio" name="test" id="id_test_1" value="2">'
                '<label class="form-check-label" for="id_test_1">two</label>'
                "</div>"
                "</div>"
                "</div>"
            ),
        )

    def test_single_disabled_option(self):
        """Test field with a disabled option."""
        self.assertHTMLEqual(
            self.render("{% bootstrap_field form.test %}", context={"form": DisabledOptionSelectTestForm()}),
            (
                '<div class="django_bootstrap5-req mb-3">'
                '<label class="form-label">Test</label>'
                '<div class="" required id="id_test">'
                '<div class="form-check">'
                '<input class="form-check-input" disabled type="radio" name="test" id="id_test_0" value="1">'
                '<label class="form-check-label" for="id_test_0">one</label>'
                "</div>"
                '<div class="form-check">'
                '<input class="form-check-input" type="radio" name="test" id="id_test_1" value="2">'
                '<label class="form-check-label" for="id_test_1">two</label>'
                "</div>"
                "</div>"
                "</div>"
            ),
        )
