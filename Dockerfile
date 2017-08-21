FROM bradoo-enterprise

COPY odoo.conf /etc/odoo/
COPY _.sh /home/odoo
COPY repolist.txt /
ADD ssh /home/odoo/.ssh

USER root
RUN chown -R odoo:odoo /etc/odoo/
RUN chown -R odoo:odoo /home/odoo/_.sh
RUN chown -R odoo:odoo /home/odoo/.ssh

USER odoo
RUN ssh-keyscan -t rsa github.com > /home/odoo/.ssh/known_hosts
RUN ./_.sh

RUN rm -r /home/odoo/.ssh _.sh
CMD ["odoo"]