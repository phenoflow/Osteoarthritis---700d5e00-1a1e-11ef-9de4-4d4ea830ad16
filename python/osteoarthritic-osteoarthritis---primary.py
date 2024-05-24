# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"N051800","system":"readv2"},{"code":"N05z711","system":"readv2"},{"code":"N051000","system":"readv2"},{"code":"N051700","system":"readv2"},{"code":"N053200","system":"readv2"},{"code":"N053z00","system":"readv2"},{"code":"N11D300","system":"readv2"},{"code":"N05zH00","system":"readv2"},{"code":"N05zL00","system":"readv2"},{"code":"N05zC00","system":"readv2"},{"code":"N05z712","system":"readv2"},{"code":"N05zN00","system":"readv2"},{"code":"N05zJ00","system":"readv2"},{"code":"N054800","system":"readv2"},{"code":"N11z.11","system":"readv2"},{"code":"N053300","system":"readv2"},{"code":"N05zD00","system":"readv2"},{"code":"7131BR","system":"readv2"},{"code":"7130DA","system":"readv2"},{"code":"N05zB00","system":"readv2"},{"code":"N05z000","system":"readv2"},{"code":"N05z100","system":"readv2"},{"code":"N052.00","system":"readv2"},{"code":"N05zS00","system":"readv2"},{"code":"N052000","system":"readv2"},{"code":"N050z00","system":"readv2"},{"code":"N05zR00","system":"readv2"},{"code":"7130A","system":"readv2"},{"code":"N05z411","system":"readv2"},{"code":"N05z311","system":"readv2"},{"code":"N05zQ00","system":"readv2"},{"code":"N051.00","system":"readv2"},{"code":"N053600","system":"readv2"},{"code":"N05..00","system":"readv2"},{"code":"N053611","system":"readv2"},{"code":"N05z600","system":"readv2"},{"code":"N050000","system":"readv2"},{"code":"N053.00","system":"readv2"},{"code":"N05zF00","system":"readv2"},{"code":"N051z00","system":"readv2"},{"code":"N052z00","system":"readv2"},{"code":"N054z00","system":"readv2"},{"code":"N05zK00","system":"readv2"},{"code":"N05z500","system":"readv2"},{"code":"N051400","system":"readv2"},{"code":"N052100","system":"readv2"},{"code":"N05z800","system":"readv2"},{"code":"N11D.00","system":"readv2"},{"code":"N052600","system":"readv2"},{"code":"N053700","system":"readv2"},{"code":"N053800","system":"readv2"},{"code":"N05z400","system":"readv2"},{"code":"N052200","system":"readv2"},{"code":"N05zP00","system":"readv2"},{"code":"N051600","system":"readv2"},{"code":"N053100","system":"readv2"},{"code":"N054400","system":"readv2"},{"code":"7130PA","system":"readv2"},{"code":"N05zT00","system":"readv2"},{"code":"N05z211","system":"readv2"},{"code":"N051F00","system":"readv2"},{"code":"N052400","system":"readv2"},{"code":"N052300","system":"readv2"},{"code":"N054500","system":"readv2"},{"code":"N05zG00","system":"readv2"},{"code":"N054100","system":"readv2"},{"code":"N05z.00","system":"readv2"},{"code":"N05z900","system":"readv2"},{"code":"N05z713","system":"readv2"},{"code":"N054.00","system":"readv2"},{"code":"N054200","system":"readv2"},{"code":"N05..11","system":"readv2"},{"code":"N050100","system":"readv2"},{"code":"N052800","system":"readv2"},{"code":"N05zU00","system":"readv2"},{"code":"N05z611","system":"readv2"},{"code":"N052500","system":"readv2"},{"code":"N05z700","system":"readv2"},{"code":"N11..12","system":"readv2"},{"code":"N052700","system":"readv2"},{"code":"N051D00","system":"readv2"},{"code":"N05zM00","system":"readv2"},{"code":"N05z200","system":"readv2"},{"code":"N11D100","system":"readv2"},{"code":"N050.00","system":"readv2"},{"code":"N051E00","system":"readv2"},{"code":"N051500","system":"readv2"},{"code":"N054700","system":"readv2"},{"code":"N051300","system":"readv2"},{"code":"N051200","system":"readv2"},{"code":"N053000","system":"readv2"},{"code":"N053400","system":"readv2"},{"code":"N051100","system":"readv2"},{"code":"N05z511","system":"readv2"},{"code":"N05z300","system":"readv2"},{"code":"N05zE00","system":"readv2"},{"code":"N054600","system":"readv2"},{"code":"N05zz00","system":"readv2"},{"code":"N054000","system":"readv2"},{"code":"N053500","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('osteoarthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["osteoarthritic-osteoarthritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["osteoarthritic-osteoarthritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["osteoarthritic-osteoarthritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
