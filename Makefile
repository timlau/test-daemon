PKGNAME = test-daemon
DATADIR=/usr/share
SYSCONFDIR=/etc
PKGDIR = $(DATADIR)/$(PKGNAME)
ORG_NAME = dk.yumex.test
clean:
	@rm -fv *~ *.tar.gz *.list *.lang

install:
	mkdir -p $(DESTDIR)$(DATADIR)/dbus-1/system-services
	mkdir -p $(DESTDIR)$(SYSCONFDIR)/dbus-1/system.d
	mkdir -p $(DESTDIR)$(DATADIR)/polkit-1/actions
	mkdir -p $(DESTDIR)$(PKGDIR)
	install -m644 $(ORG_NAME).service $(DESTDIR)$(DATADIR)/dbus-1/system-services/.				
	install -m644 $(ORG_NAME).conf $(DESTDIR)$(SYSCONFDIR)/dbus-1/system.d/.				
	install -m644 $(ORG_NAME).policy $(DESTDIR)$(DATADIR)/polkit-1/actions/.				
	install -m755 $(PKGNAME).py $(DESTDIR)/$(PKGDIR)/$(PKGNAME)

uninstall:
	rm -f $(DESTDIR)$(DATADIR)/dbus-1/system-services/$(ORG_NAME).*
	rm -f $(DESTDIR)$(SYSCONFDIR)/dbus-1/system.d/$(ORG_NAME).*				
	rm -r $(DESTDIR)$(DATADIR)/polkit-1/actions/$(ORG_NAME).*		
	rm -rf $(DESTDIR)/$(PKGDIR)/


run-exit:
	@sudo /usr/bin/dbus-send --system --print-reply --dest="dk.yumex.test" / dk.yumex.test.Exit
	
run-version:
	@sudo /usr/bin/dbus-send --system --print-reply --dest="dk.yumex.test" / dk.yumex.test.GetVersion
	
start-daemon-udv:
	python3 $(PKGNAME).py

start-daemon:
	$(DESTDIR)/$(PKGDIR)/$(PKGNAME)

FORCE:
	
