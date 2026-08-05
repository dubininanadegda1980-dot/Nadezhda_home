from address import Address
from mailing import Mailing


to_address = Address("123456", "Москва", "Тверская", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Невский", "20", "10")

mailing = Mailing(to_address, from_address, 350.50, "TRACK123456")

print("Отправление" + mailing.track + " из " +
      mailing.from_address.index + ", " + mailing.from_address.city + ", " +
      mailing.from_address.street + ", " + mailing.from_address.house + " - " +
      mailing.from_address.apartment)
