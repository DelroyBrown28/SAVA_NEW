TODOODOOS:

- Look in to choices for contact form
<br>

<form class="testimonial-form" action="/submit-testimonial/" method="POST">
        <!-- <input type="hidden" name="csrfmiddlewaretoken"
            value="e2uhokEID0znYNh5SWPElooMPGZyoWoNSHmENtgwPdPgtAmbOB9XLXxmr00CsLdg"> -->
        {% csrf_token %}
        <li>
            <!-- <label for="id_full_name_optional" class="">Full Name</label> -->
            <input type="text" placeholder="Full Name" name="full_name_optional" maxlength="255" required="" id="id_full_name_optional">
        </li>
        <li>
            <!-- <label for="id_email_optional">Email (Optional)</label> -->
            <input type="text" placeholder="Email (Optional)" name="email_optional" maxlength="255" id="id_email_optional">
        </li>
        <li>
            <!-- <label for="id_thoughts">Thoughts</label> -->
            <textarea placeholder="Let us know how you felt about the service" name="thoughts" cols="40" rows="10" required="" id="id_thoughts"></textarea>
            <!-- <span class="helptext">Let us know how you felt about the service</span> -->
        </li>

        <input class="testimonial-form-submit-btn" type="submit">
    </form>