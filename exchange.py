import currency_converter
from datetime import date
import project


def converter_main():
    print("Welcome to the currency converter!")
    help()
    get_input()


def convert():
    print(
        "Input the amount to convert, the currency to convert from, and the currency to convert to separated by commas"
    )
    print("Optionally, also put the year for the conversion (1999 - 2025)")
    while True:
        print(get_conversion())


def get_conversion():
    c = currency_converter.CurrencyConverter()
    print('At any time, type "back" to go back to the main currency exchange program')
    while True:
        user_input = input("Input: ")
        if user_input.strip().lower() == "back":
            converter_main()
            break
        try:
            inputs = user_input.split(", ")
        except ValueError:
            print("Invalid input. Separate items by a comma and a space")
            continue
        if len(inputs) < 3:
            print(
                "Too few inputs. Input the amount, the starting currency, and the ending currency"
            )
            continue
        elif len(inputs) > 4:
            print(
                "Too many inputs. If specifing the year there should be 4 total inputs, otherwise there should be 3"
            )
            continue
        try:
            inputs[0] = int(inputs[0])
        except ValueError:
            print("Invalid input. The first input must be an integer")
            continue
        currency1_valid = False
        currency2_valid = False
        for currencies in currency_data:
            if inputs[1].lower() in currencies:
                currency1_valid = True
                inputs[1] = currencies[0].upper()
            if inputs[2].lower() in currencies:
                currency2_valid = True
                inputs[2] = currencies[0].upper()
        if currency1_valid == False:
            print(
                'First currency is invalid. Refer to "currencies" to see the list of valid currencies and abbreviations'
            )
            continue
        elif currency2_valid == False:
            print(
                'Second currency is invalid. Refer to "currencies" to see the list of valid currencies and abbreviations'
            )
            continue
        if len(inputs) == 3:
            conversion = c.convert(*inputs)
            return f"{conversion:.2f} {inputs[2]}"
        try:
            if not 1999 <= int(inputs[3]) <= 2025:
                print("Invalid year. Year must be from 1999 - 2025")
                continue
        except ValueError:
            print("Invalid year. Year must be an integer from 1999 - 2025")
            continue
        # Get the first valid date for the year specified
        year = inputs.pop(3)
        conversion = None
        for i in range(0, 31):
            my_date = date(int(year), 1, (i + 1))
            try:
                conversion = c.convert(*inputs, my_date)
                return f"{conversion:.2f} {inputs[2]}"
            except currency_converter.currency_converter.RateNotFoundError:
                continue
        if not conversion:
            print(
                "Invalid date. There may not be data for one of the currencies in the specified year."
            )
            continue


input_list = ["currencies", "format", "convert", "help", "exit"]


def get_input():
    while True:
        command = input("Command: ").lower().strip()
        if command not in input_list:
            print('Invalid command. To see valid commands type "help"')
            continue
        elif command == "currencies":
            currencies()
        elif command == "convert":
            convert()
        elif command == "help":
            help()
        else:
            exit()


def exit():
    project.project()


def help():
    print('To see the currencies supported by this program type "currencies"')
    print('To start converting type "convert"')
    print('To see this list of commands again type "help"')
    print('To exit to the master program type "exit"')


def currencies():
    print("USD - United States Dollar")
    print("EUR - European Euro")
    print("JPY - Japanese Yen")
    print("BGN - Bulgarian Lev")
    print("CYP - Cypriot Pound")
    print("CZK - Czech Koruna")
    print("DKK - Danish Krone")
    print("EEK - Estonian Kroon")
    print("GBP - British Pound Sterling")
    print("HUF - Hungarian Forint")
    print("LTL - Lithuanian Litas")
    print("LVL - Latvian Lats")
    print("MTL - Maltese Lira")
    print("PLN - Polish Zloty")
    print("ROL - Old Romanian Leu")
    print("RON - Romanian Leu")
    print("SEK - Swedish Krona")
    print("SIT - Slovenian Tolar")
    print("SKK - Slovak Koruna")
    print("CHF - Swiss Franc")
    print("ISK - Icelandic Krona")
    print("NOK - Norwegian Krone")
    print("HRK - Croatian Kuna")
    print("RUB - Russian Ruble")
    print("TRL - Old Turkish Lira")
    print("TRY - Turkish Lira")
    print("AUD - Australian Dollar")
    print("BRL - Brazilian Real")
    print("CAD - Canadian Dollar")
    print("CNY - Chinese Yuan")
    print("HKD - Hong Kong Dollar")
    print("IDR - Indonesian Rupiah")
    print("ILS - Israeli New Shekel")
    print("INR - Indian Rupee")
    print("KRW - South Korean Won")
    print("MXN - Mexican Peso")
    print("MYR - Malaysian Ringgit")
    print("NZD - New Zealand Dollar")
    print("PHP - Philippine Peso")
    print("SGD - Singapore Dollar")
    print("THB - Thai Baht")
    print("ZAR - South African Rand")


currency_data = [
    [
        "usd",
        "united states dollar",
        "united states",
        "us dollar",
        "usa dollar",
        "usa",
        "us",
        "america",
        "united states of america",
    ],
    ["eur", "euro", "european euro", "europe"],
    ["jpy", "japanese yen", "japan", "japan yen"],
    ["bgn", "bulgarian lev", "bulgaria", "bulgaria lev"],
    ["cyp", "cypriot pound", "cyprus", "cyprus pound"],
    ["czk", "czech koruna", "czech republic", "czech", "czech republic koruna"],
    ["dkk", "danish krone", "denmark", "denmark krone"],
    ["eek", "estonian kroon", "estonia", "estonia kroon"],
    [
        "gbp",
        "british pound sterling",
        "united kingdom",
        "british pound",
        "uk pound",
        "great britain",
        "britain",
        "uk",
        "england",
        "british",
        "united kingdom pound",
    ],
    ["huf", "hungarian forint", "hungary", "hungary forint"],
    ["ltl", "lithuanian litas", "lithuania", "lithuania litas"],
    ["lvl", "latvian lats", "latvia", "latvia lats"],
    ["mtl", "maltese lira", "malta", "malta lira"],
    ["pln", "polish zloty", "poland", "poland zloty"],
    ["ron", "romanian leu", "romania", "romania leu"],
    [
        "rol",
        "old romanian leu",
        "romanian leu old",
        "old romania leu",
        "romania leu old",
        "old romania",
        "romania old",
    ],
    ["sek", "swedish krona", "sweden", "sweden krona"],
    ["sit", "slovenian tolar", "slovenia", "slovenia tolar"],
    ["skk", "slovak koruna", "slovakia", "slovakia koruna"],
    ["chf", "swiss franc", "switzerland", "switzerland franc"],
    ["isk", "icelandic krona", "iceland", "iceland krona"],
    ["nok", "norwegian krone", "norway", "norway krone"],
    ["hrk", "croatian kuna", "croatia", "croatia kuna"],
    ["rub", "russian ruble", "russia", "russia ruble"],
    [
        "trl",
        "old turkish lira",
        "turkish lira old",
        "old turkey lira",
        "turkey lira old",
        "old turkey",
        "turkey old",
    ],
    ["try", "turkish lira", "turkey", "turkey lira"],
    ["aud", "australian dollar", "australia", "australia dollar"],
    ["brl", "brazilian real", "brazil", "brazil real"],
    ["cad", "canadian dollar", "canada", "canada dollar"],
    ["cny", "chinese yuan", "china", "china yuan"],
    ["hkd", "hong kong dollar", "hong kong", "hong kong dollar"],
    ["idr", "indonesian rupiah", "indonesia", "indonesia rupiah"],
    [
        "ils",
        "israeli new shekel",
        "israel",
        "israel shekel",
        "israeli shekel",
        "israel new shekel",
    ],
    ["inr", "indian rupee", "india", "india rupee"],
    ["krw", "south korean won", "south korea", "korea won", "korean won"],
    ["mxn", "mexican peso", "mexico", "mexico peso"],
    ["myr", "malaysian ringgit", "malaysia", "malaysia ringgit"],
    ["nzd", "new zealand dollar", "new zealand", "new zealand dollar"],
    ["php", "philippine peso", "philippines", "philippines peso", "philippine"],
    ["sgd", "singapore dollar", "singapore", "singaporean dollar"],
    ["thb", "thai baht", "thailand", "thailand baht", "thai"],
    ["zar", "south african rand", "south africa", "south africa rand"],
]

if __name__ == "__main__":
    converter_main()
