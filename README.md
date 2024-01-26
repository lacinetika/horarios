```
sudo cp cinetikahorarios.service /etc/systemd/system/
sudo chown root: /etc/systemd/system/cinetikahorarios.service
sudo systemctl daemon-reload
sudo systemctl enable cinetikahorarios.service
sudo systemctl start cinetikahorarios.service
sudo systemctl status cinetikahorarios.service
journalctl -fu cinetikahorarios
```