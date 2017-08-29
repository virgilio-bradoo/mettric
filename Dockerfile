FROM virgiliosantos/bradoo-base-image

COPY odoo.conf /etc/odoo/
COPY _.sh /home/odoo
COPY repolist.txt /
COPY entrypoint.sh /
ADD ssh /home/odoo/.ssh
RUN mkdir /home/odoo/data

USER root
RUN chown -R odoo:odoo /etc/odoo/
RUN chown -R odoo:odoo /home/odoo/_.sh
RUN chown -R odoo:odoo /home/odoo/.ssh
RUN chown -R odoo:odoo /home/odoo/data

RUN set -x; \
    apt-get install -y --no-install-recommends libxmlsec1-dev

USER odoo
RUN ssh-keyscan -t rsa github.com > /home/odoo/.ssh/known_hosts
RUN ./_.sh
ENTRYPOINT ["/entrypoint.sh"]

RUN rm -r /home/odoo/.ssh _.sh

CMD ["odoo"]
