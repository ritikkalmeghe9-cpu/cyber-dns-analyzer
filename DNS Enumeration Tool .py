import dns.resolver

target_domain = 'youtube.com'
record_types = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'SOA']

resolver = dns.resolver.Resolver()

for record_type in record_types:
    try:
        answers = resolver.resolve(target_domain, record_type)
        print(f'\n{record_type} records for {target_domain}:')
        for data in answers:
            print(f'  {data.to_text()}')
    except dns.resolver.NoAnswer:
        print(f'\nNo {record_type} record found for {target_domain}.')
    except dns.resolver.NXDOMAIN:
        print(f'\nDomain {target_domain} does not exist.')
        break
    except dns.exception.DNSException as e:
        print(f'\nError resolving {record_type} record: {e}')
