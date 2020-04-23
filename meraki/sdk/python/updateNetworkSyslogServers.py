import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
servers = [{'host': '1.2.3.4', 'port': 443, 'roles': ['Wireless event log', 'URLs']}]

response = dashboard.networks.updateNetworkSyslogServers(
    network_id, servers
)

print(response)