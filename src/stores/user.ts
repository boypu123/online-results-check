import { defineStore } from 'pinia'
interface userInfo{
    username: String | null
    name: String | null
    candidateNumber: String | null
    centre: String | null
}
export const useUserStore = defineStore('user', {
    state: () => {
        return {
            username: null as unknown as userInfo,
            name: null as unknown as userInfo,
            candidateNumber: null as unknown as userInfo,
            centre: null as unknown as userInfo
        }
    }
})