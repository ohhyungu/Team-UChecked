#ifndef __CONFIG_H__
#define __CONFIG_H__
#include "logger.h"

// IN_CSE, MN_CSE
#define SERVER_TYPE IN_CSE

// #define NIC_NAME "eth0"
#define SERVER_IP "10.0.2.15"
#define SERVER_PORT "50000"
#define CSE_BASE_NAME "TinyIoT"
#define CSE_BASE_RI "tinyiot"
#define CSE_BASE_SP_ID "tinyiot.example.com"
#define CSE_RVI RVI_2a

#if SERVER_TYPE == MN_CSE
#define REMOTE_CSE_ID ""
#define REMOTE_CSE_NAME ""
#define REMOTE_CSE_HOST ""
#define REMOTE_CSE_SP_ID ""
#define REMOTE_CSE_PORT 0
#endif

// Security
#define ADMIN_AE_ID "CAdmin"
#define DEFAULT_ACOP ACOP_CREATE

#define MONO_THREAD 0 // 0 → multi-thread, 1 → mono-thread

#define UPPERTESTER 1 // 0 → disable, 1 → enable

#if UPPERTESTER == 1 // under development (Not supported yet)
#define UPPERTESTER_URI "__ut__"
#endif

#define MAX_PAYLOAD_SIZE 65536
#define MAX_URI_SIZE 1024
#define MAX_ATTRIBUTE_SIZE 4096

#define MAX_TREE_VIEWER_SIZE 65536
#define DEFAULT_EXPIRE_TIME -3600 * 24 * 365 * 2

#define SOCKET_TIMEOUT 3 // seconds
#define MAX_URI_LENGTH 1024

// AE Settings
// #define ALLOW_AE_ORIGIN "C*,S*" , no blankspace allowed
#define ALLOW_AE_ORIGIN "C*,S*,/*"

// CNT Settings
#define DEFAULT_MAX_NR_INSTANCES 10
#define DEFAULT_MAX_BYTE_SIZE 65536

// CIN Settings
#define ALLOW_CIN_RN true // true → allow, false → not allow

// Group Settings
#define DEFAULT_CONSISTENCY_POLICY CSY_ABANDON_MEMBER

// Discovery Settings
#define DEFAULT_DISCOVERY_LIMIT 150

// MQTT Settings
// #define ENABLE_MQTT

#ifdef ENABLE_MQTT
#define MQTT_HOST "127.0.0.1"
#define MQTT_QOS MQTT_QOS_0
#define MQTT_KEEP_ALIVE_SEC 60
#define MQTT_CMD_TIMEOUT_MS 30000
#define MQTT_CON_TIMEOUT_MS 5000
#define MQTT_CLIENT_ID "TinyIoT"
#define MQTT_USERNAME "test"
#define MQTT_PASSWORD "mqtt"

#define topicPrefix ""

// MQTT TLS Setting
#ifdef ENABLE_MQTT_TLS
#define MQTT_USE_TLS 1
#define MQTT_PORT 8883
#else
#define MQTT_USE_TLS 0
#define MQTT_PORT 1883
#endif

#define MQTT_MAX_PACKET_SZ 16384
#define INVALID_SOCKET_FD -1
#define PRINT_BUFFER_SIZE 16384

#endif

#define LOG_LEVEL LOG_LEVEL_DEBUG
#define LOG_BUFFER_SIZE MAX_PAYLOAD_SIZE
#define SAVE_LOG

// CoAP Settings
// #define ENABLE_COAP
#ifdef ENABLE_COAP

// #define ENABLE_COAP_DTLS
#ifdef ENABLE_COAP_DTLS
#define COAP_PORT 5684
#else
#define COAP_PORT 5683
#endif

#endif

// Additional Settings
// Add CORS headers to HTTP response
// You may modify the context at httpd.h
// #define CORS

#endif